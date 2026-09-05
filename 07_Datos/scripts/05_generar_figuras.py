"""
05_generar_figuras.py
Genera TODAS las figuras y tablas LaTeX del manuscrito a partir de los
resultados reales del pipeline -- CarniCore, Entrega 4 (2B), Enfoque 2.

MOTIVO DE ESTE SCRIPT (corrección de la Entrega 4)
--------------------------------------------------
En la versión entregada el 01/09/2026 las figuras y tablas del manuscrito
estaban versionadas como PNG/TEX sueltos, sin ningún script que las
generara, y sus cifras (1/27) no coincidían con la salida del pipeline
(0/27). La guía ISR-401, Sección 4 y criterio C5, exige que cada tabla y
cada figura del manuscrito se produzca con un script versionado.

Este script cierra ese hueco: lee ÚNICAMENTE los artefactos producidos por
los pasos 1 a 4 del pipeline y no contiene ninguna cifra escrita a mano.

Entradas (todas generadas por pasos anteriores):
    ../resultados/dataset_consolidado.csv
    ../resultados/kappa_resultados.json
    ../resultados/matriz_confusion_prf1.json
    ../resultados/bootstrap_ic95.json

Salidas:
    ../../08_Publicacion/figuras/figura_01_distribucion_categorias.png|.pdf
    ../../08_Publicacion/figuras/figura_02_estado_por_rf.png|.pdf
    ../../08_Publicacion/figuras/figura_03_acuerdo_expertos.png|.pdf
    ../../08_Publicacion/tablas/tabla_01_resultados_detector.tex
    ../../08_Publicacion/tablas/tabla_03_confusion_prf1.tex
    ../../08_Publicacion/tablas/tabla_04_acuerdo_interevaluador.tex
"""

import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

DIR = Path(__file__).resolve().parent
RESULTADOS = DIR.parent / "resultados"
FIGURAS = DIR.parent.parent / "08_Publicacion" / "figuras"
TABLAS = DIR.parent.parent / "08_Publicacion" / "tablas"

CATEGORIAS = {
    "cuantificador_vago": "C1 -- Cuantificadores\nvagos",
    "conjuncion_multiple": "C2 -- Conjunciones\nmúltiples",
    "voz_pasiva": "C3 -- Voz pasiva\nsin agente",
}


def cargar():
    """Carga los artefactos del pipeline. Falla ruidosamente si falta alguno."""
    faltan = []
    for nombre in (
        "dataset_consolidado.csv",
        "kappa_resultados.json",
        "matriz_confusion_prf1.json",
        "bootstrap_ic95.json",
    ):
        if not (RESULTADOS / nombre).exists():
            faltan.append(nombre)
    if faltan:
        raise SystemExit(
            "ERROR: faltan artefactos del pipeline en 06_Experimento/resultados/: "
            + ", ".join(faltan)
            + "\nEjecute primero: python run_all.py"
        )

    with open(RESULTADOS / "dataset_consolidado.csv", encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f))
    kappa = json.load(open(RESULTADOS / "kappa_resultados.json", encoding="utf-8"))
    conf = json.load(open(RESULTADOS / "matriz_confusion_prf1.json", encoding="utf-8"))
    boot = json.load(open(RESULTADOS / "bootstrap_ic95.json", encoding="utf-8"))
    return filas, kappa, conf, boot


def consenso(fila):
    """Regla pre-registrada: mayoría simple (>=2 de 3 expertos)."""
    votos = sum(int(fila[f"experto_{i}"]) for i in (1, 2, 3))
    return 1 if votos >= 2 else 0


def figura_01(filas):
    """Activaciones por categoría del detector."""
    n = len(filas)
    conteo = {k: 0 for k in CATEGORIAS}
    for fila in filas:
        activadas = (fila.get("categorias_activadas") or "").strip()
        if activadas and activadas != "ninguna":
            for clave in CATEGORIAS:
                if clave in activadas:
                    conteo[clave] += 1

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    etiquetas = [CATEGORIAS[k] for k in CATEGORIAS]
    valores = [conteo[k] for k in CATEGORIAS]
    barras = ax.bar(etiquetas, valores, color="#1f4e79", width=0.5)
    ax.set_ylabel(f"RF que activan la categoría (n = {n})")
    ax.set_title("Activaciones del detector léxico-sintáctico por categoría")
    ax.set_ylim(0, max(1, max(valores)) * 1.35 if max(valores) else 1)
    for barra, valor in zip(barras, valores):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 0.04,
            f"{valor}/{n}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(FIGURAS / f"figura_01_distribucion_categorias.{ext}", dpi=300)
    plt.close(fig)
    return conteo, n


def figura_02(filas):
    """Estado por RF: detector frente a consenso experto."""
    ids = [f["rf_id"] for f in filas]
    det = [int(f["ambiguo_detector"]) for f in filas]
    con = [consenso(f) for f in filas]

    fig, ax = plt.subplots(figsize=(9.6, 3.4))
    x = range(len(ids))
    ax.bar([i - 0.2 for i in x], det, width=0.4, label="Detector automático",
           color="#1f4e79")
    ax.bar([i + 0.2 for i in x], con, width=0.4, label="Consenso experto (>=2/3)",
           color="#c0504d")
    ax.set_xticks(list(x))
    ax.set_xticklabels(ids, rotation=90, fontsize=7)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["No ambiguo", "Ambiguo"])
    ax.set_title("Clasificación por requisito: detector frente a consenso experto")
    ax.legend(loc="upper left", frameon=False, fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(FIGURAS / f"figura_02_estado_por_rf.{ext}", dpi=300)
    plt.close(fig)
    return [i for i, c in zip(ids, con) if c == 1]


def figura_03(kappa):
    """Acuerdo inter-evaluador con las bandas de Landis y Koch."""
    pares = kappa["cohen_pares"]
    etiquetas = [p.replace("experto_", "E").replace("_vs_", " vs ") for p in pares]
    valores = list(pares.values())
    etiquetas.append("Fleiss (3)")
    valores.append(kappa["fleiss_consenso"])

    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    bandas = [
        (0.00, 0.20, "#f2f2f2", "Leve"),
        (0.20, 0.40, "#e2e2e2", "Aceptable"),
        (0.40, 0.60, "#d0d0d0", "Moderada"),
    ]
    for lo, hi, color, nombre in bandas:
        ax.axhspan(lo, hi, color=color, zorder=0)
        ax.text(len(valores) - 0.4, (lo + hi) / 2, nombre, fontsize=7,
                va="center", color="#555555")
    barras = ax.bar(etiquetas, valores, color="#1f4e79", width=0.5, zorder=2)
    for barra, valor in zip(barras, valores):
        ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 0.012,
                f"{valor:.4f}", ha="center", va="bottom", fontsize=8,
                fontweight="bold")
    ax.set_ylabel(r"$\kappa$")
    ax.set_ylim(0, 0.6)
    ax.set_title("Acuerdo inter-evaluador del panel experto (bandas: Landis y Koch, 1977)")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(FIGURAS / f"figura_03_acuerdo_expertos.{ext}", dpi=300)
    plt.close(fig)


def tabla_01(conteo, n):
    filas = "\n".join(
        f"{CATEGORIAS[k].replace(chr(10), ' ')} & {conteo[k]}/{n} & "
        f"{100 * conteo[k] / n:.1f}\\% \\\\"
        for k in CATEGORIAS
    )
    total = sum(1 for _ in ())  # placeholder, se recalcula abajo
    activados = conteo_total_activados
    contenido = f"""% Generada por 06_Experimento/scripts_analisis/05_generar_figuras.py
% NO EDITAR A MANO. Regenerar con: python run_all.py
\\begin{{table}}[t]
\\centering
\\caption{{Activaciones del detector por categoría sobre los {n} RF de CarniCore.}}
\\label{{tab:detector}}
\\begin{{tabular}}{{lcc}}
\\hline
\\textbf{{Categoría de patrón}} & \\textbf{{RF que la activan}} & \\textbf{{Porcentaje}} \\\\
\\hline
{filas}
\\hline
\\textbf{{Al menos una categoría}} & \\textbf{{{activados}/{n}}} & \\textbf{{{100 * activados / n:.1f}\\%}} \\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    (TABLAS / "tabla_01_resultados_detector.tex").write_text(contenido, encoding="utf-8")


def tabla_03(conf, boot):
    m = conf["matriz_confusion"]
    met = boot["metricas"]
    contenido = f"""% Generada por 06_Experimento/scripts_analisis/05_generar_figuras.py
% NO EDITAR A MANO. Regenerar con: python run_all.py
\\begin{{table}}[t]
\\centering
\\caption{{Matriz de confusión del detector frente al consenso experto
({conf['regla_consenso']}) y métricas de exactitud diagnóstica con
intervalo de confianza al 95\\,\\% por \\textit{{bootstrap}}
({boot['n_replicas']} réplicas, semilla {boot['seed']}).}}
\\label{{tab:confusion}}
\\begin{{tabular}}{{lcc}}
\\hline
 & \\textbf{{Consenso: ambiguo}} & \\textbf{{Consenso: no ambiguo}} \\\\
\\hline
\\textbf{{Detector: ambiguo}}    & VP = {m['verdaderos_positivos']} & FP = {m['falsos_positivos']} \\\\
\\textbf{{Detector: no ambiguo}} & FN = {m['falsos_negativos']} & VN = {m['verdaderos_negativos']} \\\\
\\hline
\\multicolumn{{3}}{{l}}{{Precisión = {met['precision']['punto_estimado']:.4f}
 (IC 95\\,\\%: [{met['precision']['ic95_low']:.4f}, {met['precision']['ic95_high']:.4f}])}} \\\\
\\multicolumn{{3}}{{l}}{{Exhaustividad = {met['recall']['punto_estimado']:.4f}
 (IC 95\\,\\%: [{met['recall']['ic95_low']:.4f}, {met['recall']['ic95_high']:.4f}])}} \\\\
\\multicolumn{{3}}{{l}}{{$F_1$ = {met['f1']['punto_estimado']:.4f}
 (IC 95\\,\\%: [{met['f1']['ic95_low']:.4f}, {met['f1']['ic95_high']:.4f}])}} \\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    (TABLAS / "tabla_03_confusion_prf1.tex").write_text(contenido, encoding="utf-8")


def tabla_04(kappa):
    def banda(v):
        if v < 0:
            return "pobre"
        if v <= 0.20:
            return "leve"
        if v <= 0.40:
            return "aceptable"
        if v <= 0.60:
            return "moderada"
        if v <= 0.80:
            return "sustancial"
        return "casi perfecta"

    filas = "\n".join(
        f"{p.replace('experto_', 'Experto ').replace('_vs_', ' vs. ')} & "
        f"{v:.4f} & {banda(v)} \\\\"
        for p, v in kappa["cohen_pares"].items()
    )
    fl = kappa["fleiss_consenso"]
    contenido = f"""% Generada por 06_Experimento/scripts_analisis/05_generar_figuras.py
% NO EDITAR A MANO. Regenerar con: python run_all.py
\\begin{{table}}[t]
\\centering
\\caption{{Acuerdo inter-evaluador del panel de {kappa['n_expertos']} personas
expertas sobre los {kappa['n_rf']} RF. Bandas interpretativas de Landis y Koch (1977).}}
\\label{{tab:kappa}}
\\begin{{tabular}}{{lcc}}
\\hline
\\textbf{{Comparación}} & \\textbf{{$\\kappa$}} & \\textbf{{Banda}} \\\\
\\hline
{filas}
\\hline
$\\kappa$ de Fleiss (conjunto) & {fl:.4f} & {banda(fl)} \\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    (TABLAS / "tabla_04_acuerdo_interevaluador.tex").write_text(contenido, encoding="utf-8")


def main():
    FIGURAS.mkdir(parents=True, exist_ok=True)
    TABLAS.mkdir(parents=True, exist_ok=True)

    filas, kappa, conf, boot = cargar()

    global conteo_total_activados
    conteo_total_activados = sum(1 for f in filas if int(f["ambiguo_detector"]) == 1)

    conteo, n = figura_01(filas)
    rf_consenso = figura_02(filas)
    figura_03(kappa)
    tabla_01(conteo, n)
    tabla_03(conf, boot)
    tabla_04(kappa)

    print("Figuras y tablas regeneradas desde los datos reales:")
    print(f"  RF totales analizados .............. {n}")
    print(f"  RF marcados por el detector ........ {conteo_total_activados}/{n}")
    print(f"  Activaciones por categoría ......... {conteo}")
    print(f"  RF por consenso experto (>=2/3) .... {len(rf_consenso)}/{n} "
          f"({', '.join(rf_consenso) if rf_consenso else 'ninguno'})")
    print(f"  kappa de Fleiss .................... {kappa['fleiss_consenso']}")
    print(f"  Precisión / Exhaustividad / F1 ..... {conf['precision']} / "
          f"{conf['recall']} / {conf['f1']}")
    print("\nSalidas en 08_Publicacion/figuras/ y 08_Publicacion/tablas/.")


conteo_total_activados = 0

if __name__ == "__main__":
    main()
