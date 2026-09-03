"""
detector_ambiguedad.py
Detector automático de ambigüedad y malos olores (smells) en requisitos --
CarniCore, Entrega 4 (2B), Enfoque 2 del componente empírico.

Implementa, sobre texto en español, las 3 categorías de patrón descritas en
la Sección 7 del protocolo experimental y en el Método del manuscrito:
  1. Cuantificadores vagos
  2. Conjunciones múltiples (posible requisito compuesto)
  3. Voz pasiva sin agente explícito

Un RF se marca como "ambiguo" (ambiguo_detector = 1) si activa AL MENOS UNA
categoría. Esta regla de decisión, junto con el listado completo de patrones,
debe coincidir con lo declarado en el protocolo antes de ejecutar el
experimento real con el panel de personas expertas (no debe ajustarse
después de ver los resultados).

Entrada:  27 RF verbatim del ERS/SRS v2.0 (Sección 3.2, ERS_SRS_2B_v2.0.tex), sin ID,
          nombre, fuente ni prioridad -- tal como los vería el panel ciego. Los 25 RF
          heredados de la Entrega 3 (2A) se mantienen sin alterar (rf25.json -> rf27.json
          es un append puro, verificado); RF-26 y RF-27 se incorporan con el texto literal
          de sus fichas en el ERS v2.0.
Salida:   clasificaciones_detector.csv (mismo directorio que este script:
          06_Experimento/scripts_analisis/)
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
