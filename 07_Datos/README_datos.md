# `07_Datos/` — Paquete de datos del componente empírico

**Proyecto:** CarniCore — Detección automática de patrones de ambigüedad en requisitos funcionales
**Asignatura:** Ingeniería de Requisitos (ISR-401) · UTEQ · 2026–2027 PPA
**Estructura exigida por:** Guía de desarrollo y consolidación del PFC, §7

---

## 1. Reproducción con una sola orden

```bash
python 07_Datos/scripts/run_all.py
```

Eso es todo. La orden regenera, desde los datos crudos y sin intervención manual,
la totalidad de las tablas y figuras que aparecen en el manuscrito y en el ERS.

### Preparación previa (una sola vez)

```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r 07_Datos/scripts/requirements.txt
```

### Comprobación de referencia

La guía define la prueba así: un tercero clona el repositorio en una máquina limpia,
ejecuta la orden única y obtiene exactamente las mismas tablas y figuras que aparecen
en los documentos. Para comprobarlo sin borrar nada:

```bash
bash herramientas/regenerar_checksums.sh --datos          # antes de ejecutar
python 07_Datos/scripts/run_all.py
bash herramientas/regenerar_checksums.sh --datos --check   # después: debe verificar
```

Si alguna salida cambia, es que dejó de ser reproducible y hay que averiguar por qué
antes de entregar.

---

## 2. Qué contiene cada carpeta

```
07_Datos/
├── datos_crudos/            Salida directa del instrumento, sin edición manual
├── datos_procesados/        Derivados, obtenidos únicamente por los scripts
├── scripts/                 Cadena de análisis + orquestador único (run_all.py)
├── resultados/              Tablas y figuras generadas. NUNCA se editan a mano
├── diccionario_datos.csv    Columna por columna: tipo, unidad, rango, procedencia
├── README_datos.md          Este archivo
├── LICENSE-DATA.txt         Licencia de los datos (CC BY 4.0), distinta del código
├── checksums_datos.sha256   Integridad del paquete (generado por script)
├── desviaciones.md          Diferencias respecto del protocolo pre-registrado
└── registro_deposito.md     Identificador persistente del depósito y su fecha
```

### `datos_crudos/`

| Archivo | Qué es |
|---|---|
| `Plantilla_Experto_1_ANONIMIZADA.md` | Hoja de clasificación devuelta por la persona experta 1, tal como la entregó |
| `Plantilla_Experto_2_ANONIMIZADA.md` | Ídem, persona experta 2 |
| `Plantilla_Experto_3_ANONIMIZADA.md` | Ídem, persona experta 3 |

Anonimizadas antes de depositarse: no contienen nombre, correo ni afiliación.
La correspondencia entre código de experto e identidad real se conserva
exclusivamente en la zona restringida cifrada.

### `datos_procesados/`

| Archivo | Cómo se obtuvo |
|---|---|
| `etiquetas_expertos.csv` | Transcripción tabular de las tres plantillas anteriores, sin juicio ni interpretación: sólo se pasa el valor 0/1 de cada casilla a una celda |

### `scripts/`

| Orden | Script | Entrada | Salida |
|---:|---|---|---|
| — | `extraer_rf_desde_tex.py` | `01_ERS/ERS_SRS_2B_v2.0.tex` | `rf27.json` (corpus) |
| 1 | `detector_ambiguedad.py` | `rf27.json` | `clasificaciones_detector.csv` |
| 2 | `01_importar_datos.py` | etiquetas + clasificaciones | `dataset_consolidado.csv` |
| 3 | `02_calcular_kappa.py` | dataset consolidado | `kappa_resultados.json` |
| 4 | `03_matriz_confusion_prf1.py` | dataset consolidado | `matriz_confusion_prf1.json`, `tabla_confusion.csv` |
| 5 | `04_bootstrap_ic95.py` | dataset consolidado | `bootstrap_ic95.json` |
| 6 | `05_generar_figuras.py` | resultados | figuras 01–03 y tablas 01, 03, 04 |
| 7 | `06_analisis_potencia.py` | resultados | `analisis_potencia.json`, figura 04, tabla 05 |

`run_all.py` los ejecuta en ese orden y se detiene en el primer error.
`extraer_rf_desde_tex.py` queda **fuera** de `run_all.py` a propósito: regenerar el
corpus es una decisión metodológica que se registra como desviación, no un paso
rutinario del análisis.

---

## 3. Corpus: cómo se obtiene y por qué cambió el procedimiento

Hasta la auditoría del **3 de septiembre de 2026**, `rf27.json` se mantenía a mano.
La comparación mecánica contra los argumentos de la macro `\rfitem` del `.tex`
entregado reveló que **21 de los 27 requisitos no coincidían**: el JSON conservaba la
redacción de la Entrega 3 (2A) y no recogía las precisiones —umbrales, rangos,
condiciones— incorporadas al ERS v2.0.

Es decir: **el corpus analizado no era el documento entregado.**

Desde esta versión, el corpus deja de mantenerse a mano y pasa a ser una salida
reproducible:

```bash
python 07_Datos/scripts/extraer_rf_desde_tex.py --salida 07_Datos/scripts/rf27.json
```

Para ver qué cambia sin escribir nada:

```bash
python 07_Datos/scripts/extraer_rf_desde_tex.py --comparar 07_Datos/scripts/rf27.json
```

**Esto es una corrección de una desviación de ejecución, no un ajuste post-hoc.**
El protocolo pre-registrado declara «los 27 RF del ERS v2.0»; lo que se ejecutó fue
otra cosa. La lógica del detector **no se ha tocado**. Registrado como **DEV-03** en
`desviaciones.md` y en el registro OSF.

> **Resultado de la corrección, verificado:** tras regenerar el corpus desde el `.tex`
> v2.0 y reejecutar el pipeline completo, **todas las salidas son idénticas byte a
> byte** a las anteriores. Ninguna cifra del manuscrito cambia. El detector sigue
> marcando 0 de 27. La corrección no altera ningún resultado: sólo hace que la
> procedencia del corpus sea verdadera y verificable.

---

## 4. Sobre el resultado del detector: 0 de 27

El detector no marca ningún requisito. Conviene decir con precisión qué significa eso,
porque no es un fallo de ejecución:

| Categoría | Activaciones | Causa verificada |
|---|---:|---|
| C1 — Cuantificadores vagos | 0/27 | Ninguno de los 26 patrones aparece en el corpus |
| C2 — Conjunciones múltiples | 0/27 | Umbral `>3` conectores; el máximo del corpus es **2** |
| C3 — Voz pasiva sin agente | 0/27 | Los RF usan uniformemente «El sistema deberá permitir…» |

En consecuencia VP = 0, FP = 0, FN = 4, VN = 23, y precisión = exhaustividad = F1 = 0.

Dos advertencias que deben acompañar a estas cifras allí donde se publiquen:

1. Con VP = 0 y FP = 0, la precisión es 0/0. Se reporta como 0 por convención, pero
   **es una cantidad indefinida**, no una estimación de rendimiento.
2. El intervalo de confianza bootstrap de anchura cero es un artefacto de remuestrear
   una constante. **No es una medida de incertidumbre.**

La lectura defendible es que la ambigüedad que las tres personas expertas sí perciben
(4 de 27 por consenso, con κ de Fleiss = 0,2636) **no es la que capturan los patrones
léxicos superficiales** sobre un corpus redactado con plantilla uniforme. Ese es un
hallazgo sustantivo del estudio, no un fracaso del instrumento.

---

## 5. Reglas que cumple todo dato de este paquete

Conforme al §5.1 de la guía:

- Cada dato existe en dos estados: **crudo** (sin edición manual) y **procesado**
  (obtenido únicamente por los scripts versionados).
- **Ningún número de ningún documento está escrito a mano.** Todos proceden de la
  salida de un script y se regeneran con la orden única.
- Todo conjunto de datos lleva su entrada en `diccionario_datos.csv`.
- Los datos personales se retiran antes de publicar. La capa pública contiene datos
  agregados o seudonimizados; la restringida, cifrada, conserva los originales.
- El tamaño de la muestra se justifica por escrito **antes** de analizar, en el
  protocolo, no después de ver los resultados.
- Toda diferencia respecto del protocolo se registra en `desviaciones.md` con fecha y
  motivo.
- Toda medida de acuerdo entre codificadoras va acompañada de su intervalo de confianza.
- Las amenazas a la validez se documentan de forma explícita en el manuscrito.

---

## 6. Amenazas a la validez

| Tipo | Amenaza | Mitigación aplicada |
|---|---|---|
| Constructo | «Ambigüedad» se opera como tres patrones léxicos; los expertos aplican un criterio semántico más amplio | Se reporta el desacuerdo como resultado, no se ajusta el detector para forzar coincidencia |
| Interna | El corpus procedía de una versión anterior del ERS | Corregido: DEV-03. El corpus se extrae del `.tex` entregado |
| Externa | N = 27 es la población completa de RF de **un** sistema, no una muestra | Se declara censo, no muestra. No se generaliza a otros dominios |
| Conclusión estadística | κ de Fleiss = 0,2636 con N = 27 está por debajo del κ mínimo detectable (0,5230); McNemar exacta p = 0,125 | Reportado explícitamente en `analisis_potencia.json`. El análisis de sensibilidad indica que harían falta ≈47 RF |

---

## 7. Licencias

- **Datos** de este paquete: CC BY 4.0 (`LICENSE-DATA.txt`).
- **Código** de `scripts/`: MIT (`LICENSE` en la raíz del repositorio).

Son licencias distintas y deliberadamente separadas, como exige el §7 de la guía.
