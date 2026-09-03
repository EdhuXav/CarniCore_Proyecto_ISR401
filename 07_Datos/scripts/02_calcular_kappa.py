"""
02_calcular_kappa.py
Calcula kappa de Cohen (por par de expertos) y kappa de Fleiss (consenso de
3+) sobre las etiquetas 'ambiguo'/'no ambiguo' de los 27 RF de la v2.0.

Entrada:  06_Experimento/resultados/dataset_consolidado.csv
          (generado por 01_importar_datos.py; columnas rf_id, experto_1,
          experto_2, experto_3, ambiguo_detector, categorias_activadas)
Salida:   06_Experimento/resultados/kappa_resultados.json

No inventa ni imputa valores: si el dataset consolidado no existe, el
script se detiene y pide correr 01_importar_datos.py primero con datos
reales del panel.
"""

import json
import sys
from pathlib import Path

import pandas as pd
from sklearn.metrics import cohen_kappa_score
from statsmodels.stats.inter_rater import aggregate_raters, fleiss_kappa

RUTA_ENTRADA = Path(__file__).resolve().parents[1] / "resultados" / "dataset_consolidado.csv"
RUTA_SALIDA = Path(__file__).resolve().parents[1] / "resultados" / "kappa_resultados.json"


def error_fatal(mensaje):
    print(f"\n[ERROR] {mensaje}\n", file=sys.stderr)
    sys.exit(1)


def main():
    if not RUTA_ENTRADA.exists():
        error_fatal(
            f"No se encontró '{RUTA_ENTRADA}'. Corre primero "
            "01_importar_datos.py con las etiquetas reales del panel de expertos."
        )

    df = pd.read_csv(RUTA_ENTRADA)

    columnas_expertos = ["experto_1", "experto_2", "experto_3"]
    faltantes = [c for c in columnas_expertos if c not in df.columns]
    if faltantes:
        error_fatal(f"Faltan columnas en '{RUTA_ENTRADA}': {faltantes}")

    if len(df) != 27:
        error_fatal(
            f"'{RUTA_ENTRADA}' tiene {len(df)} filas; se esperaban 27 (RF-01..RF-27)."
        )

    # Kappa de Cohen por cada par de expertos
    pares = [("experto_1", "experto_2"), ("experto_1", "experto_3"), ("experto_2", "experto_3")]
    kappas_cohen = {
        f"{a}_vs_{b}": round(float(cohen_kappa_score(df[a], df[b])), 4)
        for a, b in pares
    }

    # Kappa de Fleiss para el consenso de 3+
    tabla, _ = aggregate_raters(df[columnas_expertos].values)
    kappa_fleiss = round(float(fleiss_kappa(tabla)), 4)

    resultado = {
        "n_rf": len(df),
        "n_expertos": len(columnas_expertos),
        "cohen_pares": kappas_cohen,
        "fleiss_consenso": kappa_fleiss,
        "interpretacion_nota": (
            "Referencia estándar Landis & Koch (1977): <0=pobre, 0.00-0.20=leve, "
            "0.21-0.40=aceptable, 0.41-0.60=moderada, 0.61-0.80=sustancial, "
            "0.81-1.00=casi perfecta. La interpretación textual para el manuscrito "
            "debe redactarse manualmente citando el valor real obtenido aquí -- "
            "este script no la genera automáticamente para evitar frases "
            "pre-armadas que no reflejen matices del caso real."
        ),
    }

    RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with open(RUTA_SALIDA, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    print("Kappa de Cohen (por par):")
    for par, valor in kappas_cohen.items():
        print(f"  {par}: {valor}")
    print(f"Kappa de Fleiss (consenso de {len(columnas_expertos)}): {kappa_fleiss}")
    print(f"\nResultado escrito en: {RUTA_SALIDA}")


if __name__ == "__main__":
    main()
