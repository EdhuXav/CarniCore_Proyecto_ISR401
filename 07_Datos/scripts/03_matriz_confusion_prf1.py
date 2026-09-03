"""
03_matriz_confusion_prf1.py
Calcula la matriz de confusión, precisión, recall y F1 del detector
automático de ambigüedad (detector_ambiguedad.py) contra el consenso del
panel de expertos, sobre los 27 RF de la v2.0.

Consenso experto: se define como mayoría simple entre los 3 expertos
(>=2 de 3 marcan "ambiguo" -> consenso = ambiguo). Esta regla de decisión
debe coincidir con la declarada en el protocolo pre-registrado antes de
ejecutar el análisis; si el protocolo define otra regla (p.ej. unanimidad),
ajusta la función `consenso_mayoria` para que coincida -- no al revés.

Entrada:  06_Experimento/resultados/dataset_consolidado.csv
Salida:   06_Experimento/resultados/matriz_confusion_prf1.json
          06_Experimento/resultados/tabla_confusion.csv (para \\input en LaTeX)
"""

import json
import sys
from pathlib import Path

import pandas as pd
from sklearn.metrics import (
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

RUTA_ENTRADA = Path(__file__).resolve().parents[1] / "resultados" / "dataset_consolidado.csv"
RUTA_SALIDA_JSON = Path(__file__).resolve().parents[1] / "resultados" / "matriz_confusion_prf1.json"
RUTA_SALIDA_CSV = Path(__file__).resolve().parents[1] / "resultados" / "tabla_confusion.csv"


def error_fatal(mensaje):
    print(f"\n[ERROR] {mensaje}\n", file=sys.stderr)
    sys.exit(1)


def consenso_mayoria(row):
    """Consenso = mayoría simple (>=2 de 3 expertos marcan ambiguo)."""
    votos = int(row["experto_1"]) + int(row["experto_2"]) + int(row["experto_3"])
    return 1 if votos >= 2 else 0


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
    y_true = df["consenso_experto"]
    y_pred = df["ambiguo_detector"]

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()

    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    resultado = {
        "n_rf": len(df),
        "regla_consenso": "mayoría simple (>=2 de 3 expertos)",
        "matriz_confusion": {
            "verdaderos_negativos": int(tn),
            "falsos_positivos": int(fp),
            "falsos_negativos": int(fn),
            "verdaderos_positivos": int(tp),
        },
        "precision": round(float(precision), 4),
        "recall": round(float(recall), 4),
        "f1": round(float(f1), 4),
    }

    RUTA_SALIDA_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(RUTA_SALIDA_JSON, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    # Tabla lista para \input en el manuscrito LaTeX (formato longtable simple)
    with open(RUTA_SALIDA_CSV, "w", encoding="utf-8") as f:
        f.write("Métrica,Valor\n")
        f.write(f"Verdaderos negativos,{tn}\n")
        f.write(f"Falsos positivos,{fp}\n")
        f.write(f"Falsos negativos,{fn}\n")
        f.write(f"Verdaderos positivos,{tp}\n")
        f.write(f"Precisión,{precision:.4f}\n")
        f.write(f"Recall,{recall:.4f}\n")
        f.write(f"F1,{f1:.4f}\n")

    print("Matriz de confusión (filas=consenso experto, columnas=detector):")
    print(f"  TN={tn}  FP={fp}")
    print(f"  FN={fn}  TP={tp}")
    print(f"Precisión: {precision:.4f} | Recall: {recall:.4f} | F1: {f1:.4f}")
    print(f"\nResultados escritos en:\n  {RUTA_SALIDA_JSON}\n  {RUTA_SALIDA_CSV}")


if __name__ == "__main__":
    main()
