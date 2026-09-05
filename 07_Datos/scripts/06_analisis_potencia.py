"""
06_analisis_potencia.py
Cálculo de potencia estadística explícito -- CarniCore, Entrega 4 (2B), Enfoque 2.

MOTIVO DE ESTE SCRIPT (corrección de la Entrega 4)
--------------------------------------------------
El criterio C6 de la rúbrica admite, para los Enfoques 1 y 2, un
"power calculation explícito" como alternativa a la curva de saturación.
La entrega del 01/09/2026 no incluía ninguno de los dos y el criterio quedó
en nivel 2/4. Este script produce el cálculo faltante.

QUÉ CALCULA Y QUÉ NO
--------------------
NO calcula potencia post-hoc sobre el efecto observado. La potencia
observada es una función monótona del valor p y no aporta información
más allá de él (Hoenig y Heisey, 2001). Lo que se calcula aquí es un
ANÁLISIS DE SENSIBILIDAD: dado el N real y fijo del estudio, qué magnitud
de efecto habría sido detectable, y qué N habría hecho falta para detectar
efectos de interés. Esa es la pregunta legítima para un censo ya ejecutado.

Se reportan cuatro bloques:
  A. Referencia normativa de la guía ISR-401 (Cohen d = 0,50, alfa = 0,05,
     1 - beta = 0,80), para dejar constancia del cálculo canónico.
  B. Prueba de McNemar exacta sobre los pares discordantes reales
     (detector frente a consenso experto) y N necesario.
  C. Sensibilidad del contraste kappa != 0 con el N real de 27 RF.
  D. Prevalencia y su efecto sobre la exhaustividad estimable.

Entradas:  ../resultados/dataset_consolidado.csv
           ../resultados/matriz_confusion_prf1.json
           ../resultados/kappa_resultados.json
Salidas:   ../resultados/analisis_potencia.json
           ../../08_Publicacion/figuras/figura_04_curva_potencia.png|.pdf
           ../../08_Publicacion/tablas/tabla_05_potencia.tex
"""

import csv
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

DIR = Path(__file__).resolve().parent
RESULTADOS = DIR.parent / "resultados"
FIGURAS = DIR.parent.parent / "08_Publicacion" / "figuras"
TABLAS = DIR.parent.parent / "08_Publicacion" / "tablas"

ALFA = 0.05
POTENCIA_OBJETIVO = 0.80
Z_ALFA_2 = stats.norm.ppf(1 - ALFA / 2)
Z_BETA = stats.norm.ppf(POTENCIA_OBJETIVO)


# --------------------------------------------------------------------------
# Bloque A -- referencia normativa de la guía (Cohen, 1988)
# --------------------------------------------------------------------------
def bloque_a():
    d = 0.50
    n_por_grupo = 2 * ((Z_ALFA_2 + Z_BETA) / d) ** 2
    n_apareado = ((Z_ALFA_2 + Z_BETA) / d) ** 2
    return {
        "descripcion": "Referencia normativa de la guía ISR-401 (Sección 3): "
                       "d de Cohen = 0,50, alfa = 0,05, potencia = 0,80.",
        "d_cohen": d,
        "n_por_grupo_dos_muestras": math.ceil(n_por_grupo),
        "n_pares_muestras_apareadas": math.ceil(n_apareado),
        "nota": "Cálculo canónico de referencia. NO es el diseño de este "
                "estudio, que es un censo de N=27 RF con clasificación "
                "binaria apareada, no una comparación de medias.",
    }


# --------------------------------------------------------------------------
# Bloque B -- McNemar exacta sobre los pares discordantes reales
# --------------------------------------------------------------------------
def bloque_b(filas):
    b = c = 0  # b: detector 1 / consenso 0 ; c: detector 0 / consenso 1
    for f in filas:
        det = int(f["ambiguo_detector"])
        con = 1 if sum(int(f[f"experto_{i}"]) for i in (1, 2, 3)) >= 2 else 0
        if det == 1 and con == 0:
            b += 1
        elif det == 0 and con == 1:
            c += 1

    n_disc = b + c
    # Prueba binomial exacta bilateral sobre los discordantes, H0: p = 0,5
    p_exacta = stats.binomtest(min(b, c), n=n_disc, p=0.5).pvalue if n_disc else 1.0

    # N discordante necesario para alcanzar p < alfa en el caso extremo
    # (todos los discordantes en la misma dirección): 2 * 0,5^n < alfa
    n_disc_necesario = math.ceil(math.log(ALFA / 2) / math.log(0.5))

    # Con la tasa de discordancia observada, cuántos RF harían falta
    tasa_disc = n_disc / len(filas) if filas else 0
    n_rf_necesario = (
        math.ceil(n_disc_necesario / tasa_disc) if tasa_disc > 0 else None
    )

    return {
        "descripcion": "Prueba de McNemar exacta (binomial sobre discordantes) "
                       "entre la clasificación del detector y el consenso experto.",
        "discordantes_detector_si_consenso_no": b,
        "discordantes_detector_no_consenso_si": c,
        "n_discordantes": n_disc,
        "p_valor_exacto_bilateral": round(p_exacta, 4),
        "significativo_alfa_005": bool(p_exacta < ALFA),
        "n_discordantes_minimo_para_significacion": n_disc_necesario,
        "tasa_discordancia_observada": round(tasa_disc, 4),
        "n_rf_necesario_a_esa_tasa": n_rf_necesario,
        "interpretacion": (
            f"Con {n_disc} pares discordantes, todos en la misma dirección, "
            f"la prueba exacta arroja p = {p_exacta:.4f}. Se necesitan al menos "
            f"{n_disc_necesario} discordantes unidireccionales para alcanzar "
            f"p < {ALFA}. A la tasa de discordancia observada "
            f"({tasa_disc:.4f}), eso equivale a un corpus de aproximadamente "
            f"{n_rf_necesario} RF. El corpus de 27 RF es, por tanto, "
            "insuficiente para declarar significativa la diferencia de "
            "prevalencia, aunque la dirección del efecto sea inequívoca."
        ),
    }


# --------------------------------------------------------------------------
# Bloque C -- sensibilidad del contraste kappa != 0 con N = 27
# --------------------------------------------------------------------------
def bloque_c(filas, kappa_obs):
    n = len(filas)
    # Error estándar aproximado de kappa bajo H0 (Fleiss, Cohen y Everitt, 1969)
    # para el caso 2 x 2 con las marginales observadas del panel.
    p1 = sum(1 for f in filas
             if sum(int(f[f"experto_{i}"]) for i in (1, 2, 3)) >= 2) / n
    p2 = sum(int(f["experto_1"]) for f in filas) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    se0 = math.sqrt(pe + pe ** 2 - (p1 * p2 * (p1 + p2)
                                    + (1 - p1) * (1 - p2) * ((1 - p1) + (1 - p2)))) \
        / ((1 - pe) * math.sqrt(n))

    kappa_detectable = Z_ALFA_2 * se0 * (1 + Z_BETA / Z_ALFA_2)
    kappa_detectable = min(kappa_detectable, 1.0)

    # N necesario para detectar kappa = 0,40 (umbral "moderado" de Landis y Koch)
    objetivo = 0.40
    se0_unit = se0 * math.sqrt(n)  # SE0 para n = 1
    n_necesario = math.ceil(((Z_ALFA_2 + Z_BETA) * se0_unit / objetivo) ** 2)

    return {
        "descripcion": "Análisis de sensibilidad del contraste kappa != 0 "
                       "con el N real del censo.",
        "n_rf": n,
        "prevalencia_consenso": round(p1, 4),
        "acuerdo_esperado_por_azar_pe": round(pe, 4),
        "se_kappa_bajo_h0": round(se0, 4),
        "kappa_minimo_detectable_n27": round(kappa_detectable, 4),
        "kappa_observado_fleiss": kappa_obs,
        "kappa_objetivo_moderado": objetivo,
        "n_rf_necesario_para_kappa_040": n_necesario,
        "interpretacion": (
            f"Con N = {n} RF y alfa = {ALFA}, el menor kappa detectable con "
            f"potencia {POTENCIA_OBJETIVO} es aproximadamente "
            f"{kappa_detectable:.4f}. El kappa de Fleiss observado "
            f"({kappa_obs}) queda por debajo de ese umbral, de modo que el "
            "acuerdo del panel no es estadísticamente distinguible del azar "
            f"con este tamaño de corpus. Detectar un acuerdo moderado "
            f"(kappa = {objetivo}) con potencia {POTENCIA_OBJETIVO} exigiría "
            f"del orden de {n_necesario} RF."
        ),
    }


# --------------------------------------------------------------------------
# Bloque D -- prevalencia y exhaustividad estimable
# --------------------------------------------------------------------------
def bloque_d(conf):
    m = conf["matriz_confusion"]
    positivos = m["verdaderos_positivos"] + m["falsos_negativos"]
    # Intervalo de Wilson para la exhaustividad con 0 aciertos sobre `positivos`
    if positivos > 0:
        lo, hi = stats.binomtest(0, positivos, 0.5).proportion_ci(
            confidence_level=0.95, method="exact"
        )
    else:
        lo = hi = float("nan")
    return {
        "descripcion": "Efecto de la prevalencia sobre la precisión con que "
                       "puede estimarse la exhaustividad.",
        "positivos_segun_consenso": positivos,
        "exhaustividad_puntual": conf["recall"],
        "ic95_exacto_exhaustividad": [round(float(lo), 4), round(float(hi), 4)],
        "interpretacion": (
            f"La exhaustividad se estima sobre solo {positivos} casos positivos. "
            f"Aun con cero aciertos, el intervalo de confianza exacto al 95 % "
            f"llega hasta {float(hi):.4f}: el estudio no puede descartar que un "
            "detector con exhaustividad moderada hubiera producido este "
            "resultado por azar. Este es el límite estadístico principal del "
            "diseño y debe declararse como amenaza a la validez de conclusión."
        ),
    }


def figura(bloque_c_res):
    """Curva de potencia frente a N para el contraste kappa != 0."""
    se0_unit = bloque_c_res["se_kappa_bajo_h0"] * math.sqrt(bloque_c_res["n_rf"])
    ns = list(range(10, 401, 5))
    for kappa_verdadero, estilo, color in (
        (0.26, "--", "#c0504d"),
        (0.40, "-", "#1f4e79"),
        (0.60, ":", "#4f81bd"),
    ):
        potencias = []
        for n in ns:
            se_n = se0_unit / math.sqrt(n)
            z = kappa_verdadero / se_n - Z_ALFA_2
            potencias.append(stats.norm.cdf(z))
        plt.plot(ns, potencias, estilo, color=color,
                 label=fr"$\kappa$ verdadero = {kappa_verdadero:.2f}")

    plt.axhline(POTENCIA_OBJETIVO, color="#888888", lw=0.8)
    plt.axvline(bloque_c_res["n_rf"], color="#000000", lw=0.8)
    plt.text(bloque_c_res["n_rf"] + 5, 0.06, f"N real = {bloque_c_res['n_rf']}",
             fontsize=8)
    plt.text(300, POTENCIA_OBJETIVO + 0.02, "potencia = 0,80", fontsize=8,
             color="#555555")
    plt.xlabel("Número de requisitos funcionales evaluados (N)")
    plt.ylabel(r"Potencia del contraste $\kappa \neq 0$ ($\alpha = 0{,}05$)")
    plt.title("Curva de potencia frente al tamaño del corpus")
    plt.ylim(0, 1.02)
    plt.legend(frameon=False, fontsize=8, loc="lower right")
    plt.gca().spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    for ext in ("png", "pdf"):
        plt.savefig(FIGURAS / f"figura_04_curva_potencia.{ext}", dpi=300)
    plt.close()


def tabla(a, b, c, d):
    contenido = f"""% Generada por 06_Experimento/scripts_analisis/06_analisis_potencia.py
% NO EDITAR A MANO. Regenerar con: python run_all.py
\\begin{{table}}[t]
\\centering
\\caption{{Análisis de sensibilidad estadística del diseño
($\\alpha = 0{{,}}05$, potencia objetivo $1-\\beta = 0{{,}}80$).}}
\\label{{tab:potencia}}
\\begin{{tabular}}{{lc}}
\\hline
\\textbf{{Parámetro}} & \\textbf{{Valor}} \\\\
\\hline
Requisitos evaluados (censo completo) & {c['n_rf']} \\\\
Prevalencia de ambigüedad según consenso & {c['prevalencia_consenso']:.4f} \\\\
Pares discordantes (detector vs. consenso) & {b['n_discordantes']} \\\\
McNemar exacta, $p$ bilateral & {b['p_valor_exacto_bilateral']:.4f} \\\\
Discordantes mínimos para $p < 0{{,}}05$ & {b['n_discordantes_minimo_para_significacion']} \\\\
Corpus equivalente a esa tasa (RF) & {b['n_rf_necesario_a_esa_tasa']} \\\\
$\\kappa$ mínimo detectable con $N = {c['n_rf']}$ & {c['kappa_minimo_detectable_n27']:.4f} \\\\
$\\kappa$ de Fleiss observado & {c['kappa_observado_fleiss']:.4f} \\\\
$N$ necesario para detectar $\\kappa = 0{{,}}40$ & {c['n_rf_necesario_para_kappa_040']} \\\\
IC 95\\,\\% exacto de la exhaustividad & [{d['ic95_exacto_exhaustividad'][0]:.4f}, {d['ic95_exacto_exhaustividad'][1]:.4f}] \\\\
Referencia de la guía: $n$ por grupo ($d = 0{{,}}50$) & {a['n_por_grupo_dos_muestras']} \\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    (TABLAS / "tabla_05_potencia.tex").write_text(contenido, encoding="utf-8")


def main():
    FIGURAS.mkdir(parents=True, exist_ok=True)
    TABLAS.mkdir(parents=True, exist_ok=True)

    with open(RESULTADOS / "dataset_consolidado.csv", encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f))
    conf = json.load(open(RESULTADOS / "matriz_confusion_prf1.json", encoding="utf-8"))
    kap = json.load(open(RESULTADOS / "kappa_resultados.json", encoding="utf-8"))

    a = bloque_a()
    b = bloque_b(filas)
    c = bloque_c(filas, kap["fleiss_consenso"])
    d = bloque_d(conf)

    salida = {
        "alfa": ALFA,
        "potencia_objetivo": POTENCIA_OBJETIVO,
        "marco": "Análisis de sensibilidad (no potencia post-hoc). "
                 "Hoenig y Heisey (2001).",
        "A_referencia_guia": a,
        "B_mcnemar_exacta": b,
        "C_sensibilidad_kappa": c,
        "D_prevalencia_exhaustividad": d,
    }
    (RESULTADOS / "analisis_potencia.json").write_text(
        json.dumps(salida, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    figura(c)
    tabla(a, b, c, d)

    print("Análisis de potencia / sensibilidad completado.")
    print(f"  McNemar exacta ................ p = {b['p_valor_exacto_bilateral']:.4f} "
          f"({b['n_discordantes']} discordantes)")
    print(f"  Corpus necesario a esa tasa ... {b['n_rf_necesario_a_esa_tasa']} RF")
    print(f"  kappa mínimo detectable N=27 .. {c['kappa_minimo_detectable_n27']:.4f}")
    print(f"  kappa observado ............... {c['kappa_observado_fleiss']}")
    print(f"  N para kappa = 0,40 ........... {c['n_rf_necesario_para_kappa_040']} RF")
    print(f"  IC95 exhaustividad ............ {d['ic95_exacto_exhaustividad']}")
    print("\nSalidas: resultados/analisis_potencia.json, figura_04, tabla_05.")


if __name__ == "__main__":
    main()
