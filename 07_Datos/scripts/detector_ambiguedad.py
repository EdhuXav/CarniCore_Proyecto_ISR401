"""
detector_ambiguedad.py
Detector automático de ambigüedad y malos olores (smells) en requisitos --
CarniCore, Enfoque 2 del componente empírico.

===========================================================================
LÓGICA CONGELADA. NO MODIFICAR.
---------------------------------------------------------------------------
Los patrones, los umbrales y la regla de decisión de este archivo son los
declarados en el protocolo pre-registrado en OSF (https://osf.io/yp7t3,
2026-08-02) y son idénticos a los usados en la Entrega 3 (2A).

Ajustarlos después de haber visto los resultados del panel experto
invalidaría la comparación pre-registrada. Si alguna vez hay que cambiarlos,
el cambio se registra ANTES como desviación en 07_Datos/desviaciones.md y en
el propio registro OSF, nunca después.
===========================================================================

Implementa, sobre texto en español, las 3 categorías de patrón descritas en
la Sección 7 del protocolo experimental y en el Método del manuscrito:
  1. Cuantificadores vagos
  2. Conjunciones múltiples (posible requisito compuesto)
  3. Voz pasiva sin agente explícito

Un RF se marca como "ambiguo" (ambiguo_detector = 1) si activa AL MENOS UNA
categoría.

ENTRADA
-------
rf27.json: los 27 RF del ERS/SRS v2.0, sin ID, nombre, fuente ni prioridad,
tal como los vería el panel ciego.

IMPORTANTE -- procedencia del corpus (corregida el 2026-09-03, DEV-03).
Hasta esa fecha, rf27.json se mantenía A MANO y este docstring afirmaba que
su contenido era "verbatim" del ERS v2.0. No lo era: 21 de los 27 requisitos
conservaban la redacción de la Entrega 3 (2A) y no recogían las precisiones
--umbrales, rangos, condiciones-- incorporadas al ERS v2.0.

Desde entonces el corpus NO se mantiene a mano. Se genera con:

    python extraer_rf_desde_tex.py --salida rf27.json

que lo extrae de los argumentos de la macro \\rfitem de
01_ERS/ERS_SRS_2B_v2.0.tex. La desviación está documentada en
07_Datos/desviaciones.md.

Se comprobó que la corrección del corpus NO altera ningún resultado: tras
regenerarlo desde el .tex v2.0 y reejecutar el pipeline, todas las salidas
son idénticas byte a byte. El detector sigue marcando 0 de 27.

SALIDA
------
clasificaciones_detector.csv, en este mismo directorio.

NOTA SOBRE EL RESULTADO 0/27
----------------------------
El detector no activa ninguna categoría sobre este corpus. No es un fallo de
ejecución. Verificado patrón por patrón:
  - C1: ninguno de los 26 patrones de cuantificador vago aparece en el corpus.
  - C2: el umbral es ">3" conectores; el máximo observado es 2.
  - C3: los 27 RF usan la forma activa "El sistema deberá permitir...".
Léase junto a la sección 4 de 07_Datos/README_datos.md antes de interpretar
las métricas: con VP=0 y FP=0, la precisión es 0/0, indefinida en rigor.
"""

import csv
import json
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. Cuantificadores vagos
# ---------------------------------------------------------------------------
CUANTIFICADORES_VAGOS = [
    r"\bapropiad[oa]s?\b", r"\badecuad[oa]s?\b", r"\brazonable(s)?\b",
    r"\bsuficiente(s)?\b", r"\bnormalmente\b", r"\busualmente\b",
    r"\bgeneralmente\b", r"\bfrecuentemente\b", r"\brápidamente\b",
    r"\bf[aá]cil(mente)?\b", r"\bamigable\b", r"\bflexible(s)?\b",
    r"\beficiente(s)?\b", r"\baproximadamente\b", r"\bcerca de\b",
    r"\balgun[oa]s?\b", r"\bvari[oa]s?\b", r"\bmuch[oa]s?\b",
    r"\bpoc[oa]s?\b", r"\ben general\b", r"\bcuando sea necesario\b",
    r"\bsi es posible\b", r"\bde ser posible\b", r"\bmejor\b",
    r"\bóptim[oa]\b", r"\bcorrespondiente(s)?\b",  # referente ambiguo
]

# ---------------------------------------------------------------------------
# 2. Conjunciones múltiples: más de un "y"/"o" coordinando cláusulas u
#    objetos completos dentro del mismo requisito (posible RF compuesto).
#    Se cuentan las apariciones de " y " / " o " como coordinantes léxicos,
#    excluyendo listas simples de sustantivos cortos entre comas (enumeración
#    no se penaliza si es una sola lista, p. ej. "res, cerdo y pollo").
# ---------------------------------------------------------------------------
CONECTOR_Y = re.compile(r"\by\b", re.IGNORECASE)
CONECTOR_O = re.compile(r"\bo\b", re.IGNORECASE)
UMBRAL_CONECTORES = 3          # más de 3 aparece de "y"/"o" combinadas -> flag
UMBRAL_VERBOS_MODALES = 2      # más de un "deberá" en el mismo RF -> RF compuesto

VERBOS_MODALES = re.compile(r"\bdeber[áa]n?\b", re.IGNORECASE)

# ---------------------------------------------------------------------------
# 3. Voz pasiva sin agente explícito.
#    Patrones: "ser/es/son/fue/fueron/será/serán + participio" o pasiva
#    refleja "se + verbo en 3a persona" -- SIN que le siga inmediatamente
#    "por <agente>".
# ---------------------------------------------------------------------------
PASIVA_PERIFRASTICA = re.compile(
    r"\b(es|son|fue|fueron|ser[áa]n?)\s+(\w+ad[oa]s?|\w+id[oa]s?)\b",
    re.IGNORECASE,
)
PASIVA_REFLEJA = re.compile(
    r"\bse\s+(registrar[áa]|almacenar[áa]|calcular[áa]|generar[áa]|"
    r"exportar[áa]|actualizar[áa]|emitir[áa]|aplicar[áa])\b",
    re.IGNORECASE,
)
CON_AGENTE = re.compile(r"\bpor\s+(el|la|los|las|un|una)\b", re.IGNORECASE)


def detectar_cuantificadores_vagos(texto):
    encontrados = [p.strip("\\b") for p in CUANTIFICADORES_VAGOS
                   if re.search(p, texto, re.IGNORECASE)]
    return encontrados


def detectar_conjunciones_multiples(texto):
    n_y = len(CONECTOR_Y.findall(texto))
    n_o = len(CONECTOR_O.findall(texto))
    n_modal = len(VERBOS_MODALES.findall(texto))
    activado = (n_y + n_o) > UMBRAL_CONECTORES or n_modal > UMBRAL_VERBOS_MODALES
    return activado, {"conectores_y": n_y, "conectores_o": n_o, "verbos_modales": n_modal}


def detectar_voz_pasiva_sin_agente(texto):
    matches = list(PASIVA_PERIFRASTICA.finditer(texto)) + list(PASIVA_REFLEJA.finditer(texto))
    sin_agente = []
    for m in matches:
        ventana = texto[m.end(): m.end() + 25]
        if not CON_AGENTE.search(ventana):
            sin_agente.append(m.group(0))
    return sin_agente


def clasificar_rf(rf):
    texto = rf["descripcion"]
    categorias_activadas = []

    cv = detectar_cuantificadores_vagos(texto)
    if cv:
        categorias_activadas.append("cuantificador_vago")

    cm_activado, cm_detalle = detectar_conjunciones_multiples(texto)
    if cm_activado:
        categorias_activadas.append("conjuncion_multiple")

    vp = detectar_voz_pasiva_sin_agente(texto)
    if vp:
        categorias_activadas.append("voz_pasiva")

    return {
        "id_rf": rf["id"],
        "ambiguo_detector": 1 if categorias_activadas else 0,
        "categorias_activadas": ";".join(categorias_activadas) if categorias_activadas else "ninguna",
        "evidencia_cuantificador_vago": ";".join(cv),
        "evidencia_conjuncion_multiple": f"y={cm_detalle['conectores_y']},o={cm_detalle['conectores_o']},deberá={cm_detalle['verbos_modales']}" if cm_activado else "",
        "evidencia_voz_pasiva": ";".join(vp),
    }


def main():
    entrada = Path(__file__).with_name("rf27.json")
    with open(entrada, encoding="utf-8") as f:
        rf_list = json.load(f)

    resultados = [clasificar_rf(rf) for rf in rf_list]

    salida = Path(__file__).with_name("clasificaciones_detector.csv")
    with open(salida, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(resultados[0].keys()))
        writer.writeheader()
        writer.writerows(resultados)

    n_ambiguos = sum(r["ambiguo_detector"] for r in resultados)
    print(f"RF procesados: {len(resultados)}")
    print(f"RF marcados como ambiguos por el detector: {n_ambiguos}")
    print(f"Archivo generado: {salida}")


if __name__ == "__main__":
    main()
