"""
04_bootstrap_ic95.py
Calcula intervalos de confianza al 95% para precisión, recall y F1 del
detector vs. consenso experto, mediante bootstrap no paramétrico
(remuestreo con reemplazo a nivel de RF, 10 000 réplicas).

Con N=27 (población completa de RF, no una muestra), el bootstrap aquí no
estima incertidumbre por muestreo poblacional -- estima la variabilidad de
las métricas ante la composición específica de este conjunto de 27 RF. Esta
distinción debe explicitarse en la sección de Amenazas a la Validez del
manuscrito (ver cambios_documento_principal.md, plantilla de validez de
conclusión).

Entrada:  06_Experimento/resultados/dataset_consolidado.csv
Salida:   06_Experimento/resultados/bootstrap_ic95.json

Semilla fija (SEED=42) para reproducibilidad exacta entre corridas.
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score, precision_score, recall_score

RUTA_ENTRADA = Path(__file__).resolve().parents[1] / "resultados" / "dataset_consolidado.csv"
RUTA_SALIDA = Path(__file__).resolve().parents[1] / "resultados" / "bootstrap_ic95.json"

N_REPLICAS = 10_000
SEED = 42


def error_fatal(mensaje):
    print(f"\n[ERROR] {mensaje}\n", file=sys.stderr)
    sys.exit(1)


def consenso_mayoria(row):
    votos = int(row["experto_1"]) + int(row["experto_2"]) + int(row["experto_3"])
    return 1 if votos >= 2 else 0


def bootstrap_metric(y_true, y_pred, metric_fn, n_replicas, rng):
    n = len(y_true)
    valores = np.empty(n_replicas)
    for i in range(n_replicas):
        idx = rng.integers(0, n, size=n)
        valores[i] = metric_fn(y_true[idx], y_pred[idx], zero_division=0)
    return valores


def main():
    if not RUTA_ENTRADA.exists():
        error_fatal(
            f"No se encontró '{RUTA_ENTRADA}'. Corre primero "
            "01_importar_datos.py con las etiquetas reales del panel de expertos."
        )

    df = pd.read_csv(RUTA_ENTRADA)
    if len(df) != 27:
        error_fatal(f"'{RUTA_ENTRADA}' tiene {len(df)} filas; se esperaban 27.")

    df["consenso_experto"] = df.apply(consenso_mayoria, axis=1)
    y_true = df["consenso_experto"].to_numpy()
    y_pred = df["ambiguo_detector"].to_numpy()

    rng = np.random.default_rng(SEED)

    resultados = {}
    for nombre, fn in [
        ("precision", precision_score),
        ("recall", recall_score),
        ("f1", f1_score),
    ]:
        valores = bootstrap_metric(y_true, y_pred, fn, N_REPLICAS, rng)
        ic_low, ic_high = np.percentile(valores, [2.5, 97.5])
        resultados[nombre] = {
            "punto_estimado": round(float(fn(y_true, y_pred, zero_division=0)), 4),
            "ic95_low": round(float(ic_low), 4),
            "ic95_high": round(float(ic_high), 4),
        }

    salida = {
        "n_rf": len(df),
        "n_replicas": N_REPLICAS,
        "seed": SEED,
        "metricas": resultados,
        "nota_metodologica": (
            "N=27 es la población completa de RF de la v2.0, no una muestra de una "
            "población mayor. El bootstrap cuantifica la sensibilidad de las métricas "
            "a la composición de este conjunto específico de 27 RF, no una "
            "generalización estadística a un universo más amplio de requisitos."
        ),
    }

    RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with open(RUTA_SALIDA, "w", encoding="utf-8") as f:
        json.dump(salida, f, indent=2, ensure_ascii=False)

    for nombre, r in resultados.items():
        print(f"{nombre}: {r['punto_estimado']} (IC95%: [{r['ic95_low']}, {r['ic95_high']}])")
    print(f"\nResultado escrito en: {RUTA_SALIDA}")


if __name__ == "__main__":
    main()
