"""
run_all.py
Script maestro del pipeline de análisis terminal -- CarniCore, Entrega 4 (2B).

Ejecuta, en orden y deteniéndose en el primer error, todos los pasos que
regeneran las tablas y figuras del manuscrito a partir de los datos crudos
reales:

  1. detector_ambiguedad.py    -> clasificaciones_detector.csv (27 RF)
  2. 01_importar_datos.py      -> dataset_consolidado.csv (valida + fusiona)
  3. 02_calcular_kappa.py      -> kappa_resultados.json
  4. 03_matriz_confusion_prf1.py -> matriz_confusion_prf1.json, tabla_confusion.csv
  5. 04_bootstrap_ic95.py      -> bootstrap_ic95.json
  6. 05_generar_figuras.py     -> figuras y tablas LaTeX del manuscrito
  7. 06_analisis_potencia.py   -> analisis_potencia.json, curva de potencia

Ninguno de estos pasos genera datos de ejemplo o simulados: si falta el
archivo de entrada real (06_Experimento/resultados/etiquetas_expertos.csv,
producido por el panel de al menos 3 personas expertas), el pipeline se
detiene en el paso 2 con un mensaje explícito.

Uso:
    python run_all.py
    (o "make all" si se usa el Makefile adjunto)
"""

import subprocess
import sys
from pathlib import Path

DIR_SCRIPT = Path(__file__).resolve().parent

PASOS = [
    "detector_ambiguedad.py",
    "01_importar_datos.py",
    "02_calcular_kappa.py",
    "03_matriz_confusion_prf1.py",
    "04_bootstrap_ic95.py",
    "05_generar_figuras.py",
    "06_analisis_potencia.py",
]


def main():
    print("=" * 70)
    print("Pipeline de análisis terminal -- CarniCore Entrega 4 (2B)")
    print("=" * 70)

    for i, paso in enumerate(PASOS, start=1):
        ruta = DIR_SCRIPT / paso
        print(f"\n[{i}/{len(PASOS)}] Ejecutando {paso} ...")
        print("-" * 70)

        resultado = subprocess.run([sys.executable, str(ruta)], cwd=DIR_SCRIPT)

        if resultado.returncode != 0:
            print("\n" + "=" * 70)
            print(f"PIPELINE DETENIDO en el paso {i}/{len(PASOS)} ({paso}).")
            print("Revisa el mensaje de error anterior antes de reintentar.")
            print("=" * 70)
            sys.exit(resultado.returncode)

    print("\n" + "=" * 70)
    print("Pipeline completo. Los resultados numéricos están en")
    print("06_Experimento/resultados/ y las figuras y tablas del manuscrito en")
    print("08_Publicacion/figuras/ y 08_Publicacion/tablas/, todas regeneradas")
    print("a partir de los datos crudos. Ninguna cifra del manuscrito se")
    print("escribe a mano: si una cifra cambia, recompile el manuscrito.")
    print("=" * 70)


if __name__ == "__main__":
    main()
