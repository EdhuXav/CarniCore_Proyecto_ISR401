"""
calcular_acuerdo.py -- elemento A7: doble codificacion.

La guia pide "las dos hojas de codificacion producidas por dos integrantes
distintos sobre el mismo subconjunto del corpus, mas el calculo del
coeficiente de acuerdo y su intervalo de confianza, GENERADO POR SCRIPT".
Este es ese script.

Y el paragrafo 5.1 anade: "toda medida de acuerdo entre personas evaluadoras
o codificadoras se acompana de su intervalo de confianza". Por eso el
intervalo no es opcional aqui: se calcula siempre.

QUE NECESITA
------------
Dos archivos CSV, uno por persona codificadora, con estas columnas:

    id,codigo

  id     identificador de la unidad codificada (RF-01, ENTR-03-S07, ...).
         Debe coincidir en ambos archivos.
  codigo etiqueta asignada. Puede ser binaria (0/1) o categorica
         (funcional, calidad, restriccion, ...). El script detecta cual es.

Las dos personas codifican EL MISMO subconjunto, POR SEPARADO y SIN VERSE.
Si se ponen de acuerdo antes, el coeficiente no mide nada.

USO
---
    python calcular_acuerdo.py hoja_codificador_A.csv hoja_codificador_B.csv

    --salida RUTA      JSON de resultados (por defecto, acuerdo_resultado.json)
    --replicas N       replicas bootstrap (por defecto 10000)
    --semilla N        semilla (por defecto 42, la misma del pipeline principal)

QUE CALCULA
-----------
  - Acuerdo observado bruto (porcentaje de coincidencias).
  - Kappa de Cohen, con correccion por azar.
  - IC 95 % por bootstrap de percentiles sobre las unidades codificadas.
  - Matriz de contingencia completa.
  - Interpretacion segun Landis y Koch (1977), acompanada de la advertencia
    de que esa escala es una convencion, no un umbral estadistico.
"""

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
import csv


def leer_hoja(ruta):
    filas = {}
    with open(ruta, newline="", encoding="utf-8-sig") as f:
        lector = csv.DictReader(f)
        if lector.fieldnames is None:
            sys.exit(f"ERROR: {ruta} esta vacio.")
        campos = {c.strip().lower(): c for c in lector.fieldnames}
        if "id" not in campos or "codigo" not in campos:
            sys.exit(f"ERROR: {ruta} debe tener las columnas 'id' y 'codigo'. "
                     f"Tiene: {lector.fieldnames}")
        for n, fila in enumerate(lector, start=2):
            ident = (fila[campos["id"]] or "").strip()
            codigo = (fila[campos["codigo"]] or "").strip()
            if not ident:
                continue
            if not codigo:
                sys.exit(f"ERROR: {ruta}, linea {n}: la unidad '{ident}' no tiene "
                         f"codigo. Una casilla en blanco invalida la hoja: no se "
                         f"imputa ni se rellena.")
            if ident in filas:
                sys.exit(f"ERROR: {ruta}: la unidad '{ident}' aparece dos veces.")
            filas[ident] = codigo
    if not filas:
        sys.exit(f"ERROR: {ruta} no contiene ninguna fila utilizable.")
    return filas


def kappa_cohen(pares):
    """pares: lista de tuplas (codigo_A, codigo_B)."""
    n = len(pares)
    if n == 0:
        return None
    observado = sum(1 for a, b in pares if a == b) / n
    cuenta_a = Counter(a for a, _ in pares)
    cuenta_b = Counter(b for _, b in pares)
    categorias = set(cuenta_a) | set(cuenta_b)
    esperado = sum((cuenta_a[c] / n) * (cuenta_b[c] / n) for c in categorias)
    if esperado == 1.0:
        # Ambas personas usaron una sola categoria y la misma: kappa indefinido.
        return None
    return (observado - esperado) / (1 - esperado)


def interpretar(k):
    if k is None:
        return "indefinido"
    if k < 0:    return "peor que el azar"
    if k <= 0.20: return "leve"
    if k <= 0.40: return "aceptable"
    if k <= 0.60: return "moderado"
    if k <= 0.80: return "sustancial"
    return "casi perfecto"


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("hoja_a")
    p.add_argument("hoja_b")
    p.add_argument("--salida", default="acuerdo_resultado.json")
    p.add_argument("--replicas", type=int, default=10000)
    p.add_argument("--semilla", type=int, default=42)
    args = p.parse_args()

    a = leer_hoja(args.hoja_a)
    b = leer_hoja(args.hoja_b)

    solo_a, solo_b = set(a) - set(b), set(b) - set(a)
    if solo_a or solo_b:
        print("AVISO: las dos hojas no cubren exactamente las mismas unidades.")
        if solo_a: print(f"  Solo en A ({len(solo_a)}): {sorted(solo_a)[:10]}")
        if solo_b: print(f"  Solo en B ({len(solo_b)}): {sorted(solo_b)[:10]}")
        print("  El acuerdo se calcula solo sobre la interseccion.")
        print("  Para que A7 sea valido, ambas deben codificar el MISMO subconjunto.\n")

    comunes = sorted(set(a) & set(b))
    if not comunes:
        sys.exit("ERROR: las hojas no comparten ninguna unidad.")
    pares = [(a[i], b[i]) for i in comunes]
    n = len(pares)

    k = kappa_cohen(pares)
    acuerdo = sum(1 for x, y in pares if x == y) / n

    # IC 95 % por bootstrap de percentiles sobre las unidades.
    rng = random.Random(args.semilla)
    replicas = []
    for _ in range(args.replicas):
        muestra = [pares[rng.randrange(n)] for _ in range(n)]
        kr = kappa_cohen(muestra)
        if kr is not None:
            replicas.append(kr)
    replicas.sort()
    if replicas:
        bajo = replicas[int(0.025 * len(replicas))]
        alto = replicas[min(int(0.975 * len(replicas)), len(replicas) - 1)]
    else:
        bajo = alto = None

    contingencia = defaultdict(int)
    for x, y in pares:
        contingencia[f"{x}|{y}"] += 1

    resultado = {
        "n_unidades_codificadas": n,
        "hoja_a": str(args.hoja_a),
        "hoja_b": str(args.hoja_b),
        "categorias_observadas": sorted({c for par in pares for c in par}),
        "acuerdo_observado_bruto": round(acuerdo, 4),
        "kappa_cohen": None if k is None else round(k, 4),
        "ic95_bootstrap": {
            "low": None if bajo is None else round(bajo, 4),
            "high": None if alto is None else round(alto, 4),
            "replicas": args.replicas,
            "semilla": args.semilla,
            "metodo": "bootstrap de percentiles sobre las unidades codificadas",
        },
        "interpretacion_landis_koch": interpretar(k),
        "matriz_contingencia": dict(contingencia),
        "nota_metodologica": (
            "La escala de Landis y Koch (1977) es una convencion de lectura, no un "
            "umbral estadistico. Reporte siempre el valor y su intervalo, no solo la "
            "etiqueta cualitativa. Un IC que cruza el cero indica que el acuerdo no se "
            "distingue del azar con el tamano de muestra disponible."
        ),
    }

    Path(args.salida).write_text(
        json.dumps(resultado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("=" * 66)
    print(f"Unidades codificadas por ambas personas : {n}")
    print(f"Acuerdo observado bruto                 : {acuerdo:.4f}")
    print(f"Kappa de Cohen                          : "
          f"{'indefinido' if k is None else f'{k:.4f}'}")
    if bajo is not None:
        print(f"IC 95 % (bootstrap, semilla {args.semilla})       : [{bajo:.4f}, {alto:.4f}]")
    print(f"Interpretacion (Landis y Koch)          : {interpretar(k)}")
    print("=" * 66)
    print(f"Resultado escrito en: {args.salida}")
    if bajo is not None and bajo < 0 < alto:
        print("\nAVISO: el intervalo cruza el cero. Con este numero de unidades, el")
        print("acuerdo observado no se distingue del azar. Reportelo asi, y no")
        print("aumente la muestra selectivamente hasta que salga significativo.")


if __name__ == "__main__":
    main()
