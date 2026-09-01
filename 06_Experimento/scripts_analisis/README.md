# `06_Experimento/scripts_analisis/` — Pipeline reproducible del análisis terminal

Este directorio regenera **todas** las tablas y figuras del componente empírico
(RQ1: detector de ambigüedad vs. panel de expertos) a partir de datos reales,
sin intervención manual.

## Requisito previo — dato que este pipeline NO genera

Antes de correr nada, debe existir:

```
06_Experimento/datos_procesados/etiquetas_expertos.csv
```

con las columnas `rf_id, experto_1, experto_2, experto_3` (valores 0/1),
producidas por al menos 3 personas expertas en IR clasificando los 27 RF de
forma **ciega e independiente**, según el protocolo pre-registrado
(`06_Experimento/protocolo.pdf`). Este pipeline no crea, simula ni imputa
ese archivo — si no existe, el paso 2 se detiene con un error explícito.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución completa

```bash
python run_all.py
# o
make all
```

## Qué hace cada paso

| # | Script | Entrada | Salida |
|---|---|---|---|
| 1 | `detector_ambiguedad.py` | `rf27.json` (27 RF verbatim del ERS v2.0) | `clasificaciones_detector.csv` |
| 2 | `01_importar_datos.py` | `etiquetas_expertos.csv` + `clasificaciones_detector.csv` | `dataset_consolidado.csv` (valida esquema, 27/27 RF, sin duplicados) |
| 3 | `02_calcular_kappa.py` | `dataset_consolidado.csv` | `kappa_resultados.json` (κ Cohen por par, κ Fleiss consenso) |
| 4 | `03_matriz_confusion_prf1.py` | `dataset_consolidado.csv` | `matriz_confusion_prf1.json`, `tabla_confusion.csv` (precisión/recall/F1) |
| 5 | `04_bootstrap_ic95.py` | `dataset_consolidado.csv` | `bootstrap_ic95.json` (IC 95%, 10 000 réplicas, semilla fija=42) |

Todas las salidas se escriben en `06_Experimento/resultados/`.

## Regla de consenso experto

Mayoría simple: un RF se considera "ambiguo" según el panel si **≥2 de 3**
expertos lo marcaron como tal. Esta regla está fijada en
`03_matriz_confusion_prf1.py` (función `consenso_mayoria`) y
`04_bootstrap_ic95.py`. Si el protocolo pre-registrado define una regla
distinta (p. ej. unanimidad), ajusta esa función para que coincida con lo
declarado — nunca al revés, para no introducir sesgo post-hoc.

## Reglas de detección del detector automático

El criterio de `detector_ambiguedad.py` (cuantificadores vagos, conjunciones
múltiples, voz pasiva sin agente) es el mismo que se usó en la Entrega 3
(2A) sobre 25 RF, **sin modificar**, extendido ahora a los 27 RF de la v2.0
(`rf27.json` = `rf25.json` + RF-26 + RF-27, verificado como *append* puro).
No se debe ajustar esta lógica después de ver los resultados del panel de
expertos — eso invalidaría la comparación pre-registrada.

## Limpieza

```bash
make clean
```

Borra únicamente los artefactos generados por el pipeline. Nunca borra
`etiquetas_expertos.csv`, que es dato crudo real.
