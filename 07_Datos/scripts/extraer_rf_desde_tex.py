"""
extraer_rf_desde_tex.py
Extractor determinista del corpus de requisitos funcionales -- CarniCore.

MOTIVO DE EXISTENCIA
--------------------
Hasta la version anterior, el corpus sobre el que corre el detector
(`rf27.json`) se mantenia a mano. La auditoria del 3 de septiembre de 2026
comparo, requisito por requisito, el contenido de `rf27.json` con los
argumentos de la macro \\rfitem del documento entregado
(`01_ERS/ERS_SRS_2B_v2.0.tex`) y encontro que 21 de los 27 requisitos NO
coincidian: `rf27.json` conservaba la redaccion de la Entrega 3 (2A) y no
recogia las precisiones (umbrales, rangos, condiciones) incorporadas al ERS
v2.0.

El corpus analizado, por tanto, no era el documento entregado. Este script
elimina la posibilidad de que eso vuelva a ocurrir: el corpus deja de ser un
archivo mantenido a mano y pasa a ser una SALIDA reproducible del .tex.

Esto es una correccion de una desviacion de ejecucion respecto del protocolo
pre-registrado (que declara "los 27 RF del ERS v2.0"), NO un ajuste post-hoc
de la logica de deteccion. La logica del detector no se toca. Registrese como
DEV-03 en `06_Experimento/osf_deviations.pdf`.

USO
---
    python extraer_rf_desde_tex.py                      # escribe rf27_v2.json
    python extraer_rf_desde_tex.py --salida rf27.json   # sobrescribe el corpus
    python extraer_rf_desde_tex.py --comparar rf27.json # solo informa, no escribe

SALIDA
------
JSON con la misma forma que el corpus historico:
    [{"id": "RF-01", "nombre": "...", "descripcion": "..."}, ...]

El texto se normaliza SOLO en lo imprescindible para que sea lenguaje natural
y no marcado: se deshacen comandos de LaTeX de formato, comillas dobles
tipograficas y escapes. No se elimina, resume ni reescribe contenido. La
normalizacion es deterministica y esta enteramente contenida en la funcion
`limpiar_latex`, de modo que sea auditable de un vistazo.
"""

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TEX_POR_DEFECTO = RAIZ / "01_ERS" / "ERS_SRS_2B_v2.0.tex"

# La macro del ERS es:
#   \rfitem{ID}{Nombre}{Descripcion}{Fuente}{Prioridad}{Estabilidad}{CA}{Deps}
POSICION_ID = 0
POSICION_NOMBRE = 1
POSICION_DESCRIPCION = 2
N_ARGUMENTOS = 8


def leer_grupo_llaves(texto, inicio):
    """Devuelve (contenido, indice_siguiente) del grupo {...} que abre en `inicio`.

    Cuenta llaves equilibradas y respeta los escapes \\{ y \\}, de modo que
    funciona con descripciones que contienen matematicas o llaves anidadas.
    """
    if texto[inicio] != "{":
        raise ValueError(f"Se esperaba '{{' en la posicion {inicio}")
    profundidad = 0
    i = inicio
    while i < len(texto):
        c = texto[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            profundidad += 1
        elif c == "}":
            profundidad -= 1
            if profundidad == 0:
                return texto[inicio + 1:i], i + 1
        i += 1
    raise ValueError("Grupo de llaves sin cerrar")


def limpiar_latex(s):
    """Convierte el argumento LaTeX en texto plano, sin alterar el contenido."""
    # Comandos de formato que envuelven texto: se conserva el texto interior.
    for macro in ("textbf", "textit", "emph", "texttt", "textsc", "url", "text"):
        s = re.sub(r"\\" + macro + r"\{([^{}]*)\}", r"\1", s)
    # Referencias cruzadas: no aportan texto legible al analista.
    s = re.sub(r"\\(?:cite|ref|label|nameref|autoref)\{[^{}]*\}", "", s)
    # Comillas dobles tipograficas de LaTeX.
    s = s.replace("``", '"').replace("''", '"')
    # Simbolos matematicos frecuentes en los umbrales del ERS v2.0.
    reemplazos = {
        r"\$\\pm\$": "+/-", r"\\pm": "+/-",
        r"\$\\leq\$": "<=", r"\\leq": "<=",
        r"\$\\geq\$": ">=", r"\\geq": ">=",
        r"\$<\$": "<", r"\$>\$": ">",
    }
    for patron, valor in reemplazos.items():
        s = re.sub(patron, valor, s)
    # Escapes de caracteres reservados.
    s = re.sub(r"\\([%&_#$\{\}])", r"\1", s)
    # Guiones largos de LaTeX.
    s = s.replace("---", "\u2014").replace("--", "\u2013")
    # Espaciado no separable y restos de espaciado explicito.
    s = s.replace("~", " ").replace("\\,", " ").replace("\\ ", " ")
    # Cualquier macro remanente sin argumentos.
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    # Colapso de espacios.
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extraer(ruta_tex):
    texto = Path(ruta_tex).read_text(encoding="utf-8", errors="strict")
    requisitos = []
    vistos = set()

    for m in re.finditer(r"\\rfitem\b", texto):
        # La definicion \newcommand{\rfitem}[8]{...} tambien contiene la cadena;
        # se descarta comprobando que el primer argumento tenga forma de ID.
        i = texto.find("{", m.end())
        if i == -1:
            continue
        try:
            argumentos = []
            pos = i
            for _ in range(N_ARGUMENTOS):
                arg, pos = leer_grupo_llaves(texto, pos)
                argumentos.append(arg)
                while pos < len(texto) and texto[pos] in " \t\r\n":
                    pos += 1
                if pos < len(texto) and texto[pos] != "{":
                    break
        except (ValueError, IndexError):
            continue

        if len(argumentos) < 3:
            continue
        identificador = limpiar_latex(argumentos[POSICION_ID])
        if not re.fullmatch(r"RF-\d{2}", identificador):
            continue
        if identificador in vistos:
            print(f"AVISO: {identificador} aparece mas de una vez; se conserva la primera.",
                  file=sys.stderr)
            continue
        vistos.add(identificador)
        requisitos.append({
            "id": identificador,
            "nombre": limpiar_latex(argumentos[POSICION_NOMBRE]),
            "descripcion": limpiar_latex(argumentos[POSICION_DESCRIPCION]),
        })

    requisitos.sort(key=lambda r: int(r["id"].split("-")[1]))
    return requisitos


def comparar(nuevos, ruta_previa):
    previos = {r["id"]: r for r in json.loads(Path(ruta_previa).read_text(encoding="utf-8"))}
    distintos = 0
    print(f"Comparacion contra {ruta_previa}")
    print("=" * 72)
    for r in nuevos:
        anterior = previos.get(r["id"])
        if anterior is None:
            print(f"[NUEVO ] {r['id']} no existia en el corpus anterior")
            distintos += 1
        elif anterior["descripcion"] != r["descripcion"]:
            distintos += 1
            print(f"\n[DISTINTO] {r['id']}")
            print(f"  anterior: {anterior['descripcion']}")
            print(f"  .tex    : {r['descripcion']}")
    solo_previos = set(previos) - {r["id"] for r in nuevos}
    for i in sorted(solo_previos):
        print(f"[AUSENTE] {i} estaba en el corpus anterior y no en el .tex")
        distintos += 1
    print("=" * 72)
    print(f"Requisitos con texto distinto: {distintos} de {len(nuevos)}")
    return distintos


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--tex", default=str(TEX_POR_DEFECTO),
                   help="Ruta del .tex del ERS (por defecto, el del repositorio).")
    p.add_argument("--salida", default=None,
                   help="Archivo JSON a escribir. Si se omite, se escribe rf27_v2.json "
                        "junto a este script.")
    p.add_argument("--comparar", default=None,
                   help="Compara contra un corpus existente y NO escribe nada.")
    args = p.parse_args()

    requisitos = extraer(args.tex)
    print(f"Requisitos extraidos de {args.tex}: {len(requisitos)}")

    if args.comparar:
        comparar(requisitos, args.comparar)
        return

    salida = Path(args.salida) if args.salida else Path(__file__).with_name("rf27_v2.json")
    salida.write_text(
        json.dumps(requisitos, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Corpus escrito en: {salida}")
    print("Recuerde: NO modifique la logica de detector_ambiguedad.py. "
          "Reejecute el pipeline y registre la desviacion DEV-03.")


if __name__ == "__main__":
    main()
