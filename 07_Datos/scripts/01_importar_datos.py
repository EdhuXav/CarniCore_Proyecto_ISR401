"""
01_importar_datos.py
Primer paso del pipeline de análisis terminal -- CarniCore, Entrega 4 (2B).

Este script NO genera datos: valida que el archivo de etiquetas del panel de
expertos exista, tenga el esquema correcto y esté completo, y lo deja listo
para los pasos siguientes (02_calcular_kappa.py, 03_matriz_confusion_prf1.py).

Si el archivo de entrada no existe todavía, el script se detiene con un
mensaje explícito -- por diseño. Este pipeline no debe producir resultados
con datos simulados o de relleno: los gatekeepers G4/G5 penalizan
exactamente ese patrón. Ejecuta este script solo cuando el panel de
mínimo 3 personas expertas haya completado la clasificación real.

Entrada esperada:  06_Experimento/datos_procesados/etiquetas_expertos.csv
                    Columnas: rf_id, experto_1, experto_2, experto_3
                    Valores de experto_N: 0 (no ambiguo) / 1 (ambiguo)
                    Debe contener exactamente los 27 RF (RF-01..RF-27),
                    en cualquier orden, sin filas repetidas ni vacías.

Salida:             06_Experimento/resultados/dataset_consolidado.csv
                    (etiquetas de expertos + clasificación del detector,
                    unidas por rf_id, lista para 02_calcular_kappa.py y
                    03_matriz_confusion_prf1.py)
"""

import csv
import sys
from pathlib import Path

RF_ESPERADOS = {f"RF-{i:02d}" for i in range(1, 28)}
COLUMNAS_ESPERADAS = ["rf_id", "experto_1", "experto_2", "experto_3"]

RUTA_ETIQUETAS = Path(__file__).resolve().parents[1] / "datos_procesados" / "etiquetas_expertos.csv"
RUTA_DETECTOR = Path(__file__).with_name("clasificaciones_detector.csv")
RUTA_SALIDA = Path(__file__).resolve().parents[1] / "resultados" / "dataset_consolidado.csv"


def error_fatal(mensaje):
    print(f"\n[ERROR] {mensaje}\n", file=sys.stderr)
    sys.exit(1)


def cargar_etiquetas_expertos(ruta):
    if not ruta.exists():
        error_fatal(
            f"No se encontró '{ruta}'.\n"
            "Este archivo debe contener la clasificación real del panel de al menos\n"
            "3 personas expertas en IR sobre los 27 RF (ambiguo=1 / no ambiguo=0),\n"
            "recolectada de forma ciega e independiente (ver protocolo.pdf, Sección\n"
            "'Comparación'). No generes este archivo con datos de ejemplo: el pipeline\n"
            "está diseñado para detenerse aquí hasta que el panel real esté completo."
        )

    with open(ruta, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    if not filas:
        error_fatal(f"'{ruta}' existe pero está vacío.")

    columnas = list(filas[0].keys())
    faltantes = [c for c in COLUMNAS_ESPERADAS if c not in columnas]
    if faltantes:
        error_fatal(
            f"Faltan columnas obligatorias en '{ruta}': {faltantes}. "
            f"Columnas encontradas: {columnas}"
        )

    rf_ids = [fila["rf_id"] for fila in filas]
    duplicados = {rid for rid in rf_ids if rf_ids.count(rid) > 1}
    if duplicados:
        error_fatal(f"IDs de RF duplicados en '{ruta}': {sorted(duplicados)}")

    faltan_rf = RF_ESPERADOS - set(rf_ids)
    if faltan_rf:
        error_fatal(
            f"'{ruta}' no cubre los 27 RF de la v2.0. Faltan: {sorted(faltan_rf)}"
        )

    sobran_rf = set(rf_ids) - RF_ESPERADOS
    if sobran_rf:
        error_fatal(
            f"'{ruta}' contiene IDs que no existen en el ERS v2.0: {sorted(sobran_rf)}"
        )

    for fila in filas:
        for col in ("experto_1", "experto_2", "experto_3"):
            valor = fila[col].strip()
            if valor not in ("0", "1"):
                error_fatal(
                    f"Valor inválido '{valor}' en columna '{col}' para {fila['rf_id']}. "
                    "Se esperaba 0 (no ambiguo) o 1 (ambiguo)."
                )

    return filas


def cargar_clasificaciones_detector(ruta):
    if not ruta.exists():
        error_fatal(
            f"No se encontró '{ruta}'. Ejecuta primero detector_ambiguedad.py "
            "para generar clasificaciones_detector.csv sobre rf27.json."
        )
    with open(ruta, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    ids_detector = {fila["id_rf"] for fila in filas}
    if ids_detector != RF_ESPERADOS:
        error_fatal(
            f"'{ruta}' no cubre exactamente los 27 RF esperados. "
            f"Diferencia: {RF_ESPERADOS.symmetric_difference(ids_detector)}. "
            "¿Corriste detector_ambiguedad.py sobre rf27.json (no rf25.json)?"
        )
    return {fila["id_rf"]: fila for fila in filas}


def consolidar(etiquetas, detector):
    consolidado = []
    for fila in etiquetas:
        rf_id = fila["rf_id"]
        det = detector[rf_id]
        consolidado.append({
            "rf_id": rf_id,
            "experto_1": fila["experto_1"],
            "experto_2": fila["experto_2"],
            "experto_3": fila["experto_3"],
            "ambiguo_detector": det["ambiguo_detector"],
            "categorias_activadas": det["categorias_activadas"],
        })
    return sorted(consolidado, key=lambda r: int(r["rf_id"].split("-")[1]))


def main():
    print(f"Buscando etiquetas del panel de expertos en: {RUTA_ETIQUETAS}")
    etiquetas = cargar_etiquetas_expertos(RUTA_ETIQUETAS)
    print(f"  -> {len(etiquetas)} RF encontrados y validados (27/27 esperados).")

    print(f"Buscando clasificaciones del detector en: {RUTA_DETECTOR}")
    detector = cargar_clasificaciones_detector(RUTA_DETECTOR)
    print(f"  -> {len(detector)} RF encontrados y validados (27/27 esperados).")

    consolidado = consolidar(etiquetas, detector)

    RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with open(RUTA_SALIDA, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(consolidado[0].keys()))
        writer.writeheader()
        writer.writerows(consolidado)

    print(f"\nDataset consolidado escrito en: {RUTA_SALIDA}")
    print("Listo para 02_calcular_kappa.py y 03_matriz_confusion_prf1.py.")


if __name__ == "__main__":
    main()
