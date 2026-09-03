# Changelog

Todas las modificaciones relevantes de este proyecto se documentan aquí.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el versionado sigue [Versionado Semántico](https://semver.org/lang/es/).

Correspondencia entre versiones y entregas del PFC:

|Versión|Entrega|Semana|
|-|-|-|
|0.1.0|Entrega 1 (1A)|4|
|0.5.0|Entrega 2 (1B)|10|
|1.0.0|Entrega 3 (2A)|13|
|2.0.0|Entrega 4 (2B / Defensa)|17|
|2.1.0|Correcciones para el examen final|19|

\---

## \[2.1.0] — 2026-09-04 — Correcciones para el examen final

Versión que responde al informe docente del 1 de septiembre de 2026.

### Corregido

* **Manuscrito: se reportan los resultados reales.** La versión 2.0.0 declaraba
en DEV-01 que la fase comparativa contra el panel experto no se había
ejecutado, y reportaba que el detector marcó 1 de 27 requisitos (3,7 %)
atribuyendo la activación a RF-27 por el término *correspondientes*. Las tres
afirmaciones eran incorrectas. El panel se ejecutó, sus etiquetas estaban
versionadas y el detector marcó **0 de 27**. El texto citado no existe en
RF-27. Ver `06\\\_Experimento/osf\\\_deviations.pdf`, apartado COR-01.
* **Manuscrito: plantilla oficial.** Se sustituyó `\\\\documentclass{article}` por
`\\\\documentclass\\\[runningheads]{llncs}`, la clase oficial de Springer LNCS
exigida por el criterio C7 y el gatekeeper G2.
* **`splncs04.bst` reparado.** El archivo del repositorio invocaba las funciones
`new.block.checkb`, `new.sentence.checka` y `new.sentence.checkb` sin
definirlas, lo que hacía abortar a BibTeX con 52 errores. Se añadieron las
tres definiciones.
* **`checksums.sha256` regenerado.** De las 86 entradas anteriores fallaban 7:
dos rutas heredadas de la Entrega 3 (`01\\\_ERS/main.tex` y
`01\\\_ERS/figura/istar\\\_SD.svg`) ya no existían y cinco archivos tenían hash
distinto del declarado. Además el manifiesto no cubría ningún archivo
multimedia. El nuevo manifiesto tiene 468 entradas, incluye los 22 archivos
multimedia y contenedores, y verifica sin error.
* **Identificador del registro OSF corregido.** Los documentos citaban
`osf.io/wud69`, que es el identificador del *proyecto*. El identificador del
*registro* es `osf.io/yp7t3`, y es público desde su creación. Se propagó el
identificador correcto a los seis documentos donde aparecía. Con ello el
indicador FAIR A4 pasa a cumplido.
* **Autoevaluación FAIR corregida.** La versión anterior se adjudicaba 16/16
indicadores (100 %) mientras el manifiesto de integridad fallaba. La nueva
evaluación reconoce 14/16 (87,5 %) y detalla los dos indicadores no cumplidos
con su plan de subsanación.
* **`README.md`**: se eliminó la afirmación de 90 respuestas del cuestionario
(el CSV tiene 31), la insignia de FAIR 100 % y la marca de reproducibilidad
del pipeline sobre las figuras del manuscrito, que hasta ahora no era cierta.
* **`README\\\_dataset.md`**: se eliminaron los marcadores de posición
«\[cuando haya panel experto]» y «\[PENDIENTE panel experto]», se corrigió el
listado de archivos (varios no existían) y se sustituyó `run\\\_all.sh` por
`run\\\_all.py`.
* **`fichas\\\_tecnicas.csv`**: se corrigió la nota de ENTR-15, que afirmaba haber
verificado manualmente una duración distinta a la de ENTR-14. Los dos vídeos
son el mismo archivo (idéntico tamaño e idéntico CRC32). Ver
`02\\\_Evidencias/00\\\_Restringido/INCIDENCIA\\\_ENTR14\\\_ENTR15.md`.

### Añadido

* `06\\\_Experimento/scripts\\\_analisis/05\\\_generar\\\_figuras.py`: genera todas las
figuras y tablas de resultados del manuscrito desde los artefactos del
pipeline. Cierra la causa raíz del error del manuscrito: ya no es posible que
documento y datos diverjan sin que se note.
* `06\\\_Experimento/scripts\\\_analisis/06\\\_analisis\\\_potencia.py`: cálculo de potencia
explícito exigido por el criterio C6 (McNemar exacta, κ mínimo detectable,
N necesario, IC exacto de la exhaustividad).
* `06\\\_Experimento/osf\\\_deviations.pdf` y `.tex`: documento de desviaciones
respecto del pre-registro, ausente en la entrega anterior.
* `herramientas/regenerar\\\_checksums.sh`: regenera y verifica el manifiesto.
* `herramientas/verificar\\\_dois.py`: verifica cada DOI del `.bib` contra Crossref
y propone candidatos para las entradas sin DOI.
* `herramientas/enmascarar\\\_consentimientos.py`: instrumento para cubrir nombre,
firma y correo en las copias públicas de los consentimientos.
* `02\\\_Evidencias/Codificacion\\\_Tematica/curva\\\_saturacion.py` y su plantilla de
datos, para producir la curva a partir de la codificación real del equipo.
* `.mailmap`: consolida las identidades duplicadas de Git de dos integrantes.
* `09\\\_Defensa/guion\\\_defensa\\\_v2.md`: guion de 25 minutos con reparto equitativo
y el contenido de las siete láminas del componente empírico que faltaban.
* `resumen\\\_modificaciones.md`: informe detallado de esta versión.
* Bibliografía ampliada de 18 a 62 entradas.
* Figuras 03 (acuerdo inter-evaluador) y 04 (curva de potencia), y tablas 03, 04
y 05, todas generadas por script.

### Cambiado

* Destino de publicación: de REFSQ 2027 Research Previews (8 páginas) a REFSQ
2027 track Research (15 páginas). El manuscrito corregido no cabe en ocho
páginas con el trabajo relacionado ampliado, el análisis de sensibilidad y las
ocho amenazas a la validez.
* Título del manuscrito, para que refleje el hallazgo real.
* `run\\\_all.py` y `Makefile`: el pipeline pasa de 5 a 7 pasos.
* `CITATION.cff`: versión 2.1.0 y eliminación del texto de marcador de posición
sobre el DOI.

\---

## \[2.0.0] — 2026-09-01 — Entrega 4 (2B / Defensa Final)

### Añadido

* ERS/SRS v2.0 definitivo unificado (135 páginas) con las observaciones de la
Entrega 3 resueltas, incorporando RF-26 y RF-27.
* Tercera ronda de trabajo de campo: entrevistas ENTR-06 a ENTR-16.
* Panel de tres personas expertas: rúbrica, plantillas anonimizadas y
`etiquetas\\\_expertos.csv`.
* Pipeline de análisis: `01\\\_importar\\\_datos.py`, `detector\\\_ambiguedad.py`,
`02\\\_calcular\\\_kappa.py`, `03\\\_matriz\\\_confusion\\\_prf1.py`, `04\\\_bootstrap\\\_ic95.py`,
`run\\\_all.py`, `Makefile` y `requirements.txt`.
* Depósito Zenodo con DOI persistente y archivado en Software Heritage.
* `09\\\_Defensa/` con presentación, guion, vídeo y folleto de una hoja.
* `fair\\\_assessment.pdf`, `CITATION.cff` v2.0.0 y `LICENSE` con alcance explícito.

### Cambiado

* Matriz de trazabilidad ampliada a 60 filas.
* MVP: backend Node/Express/Sequelize con 15 controladores y `docker-compose`.

\---

## \[1.0.0] — 2026-08-02 — Entrega 3 (2A)

### Añadido

* ERS/SRS completo con 25 RF y 15 RNF.
* Protocolo experimental del Enfoque 2 y su registro en OSF (`wud69`).
* Segunda ronda de campo: entrevistas ENTR-01 a ENTR-05 y cuestionario.
* Paquete ético A01–A13 y `Adenda\\\_Segunda\\\_Ronda.pdf`.
* Borrador del manuscrito: introducción, trabajo relacionado y metodología.
* Modelado UML y primeros mockups.

\---

## \[0.5.0] — 2026-06 — Entrega 2 (1B)

### Añadido

* ERS/SRS parcial con la primera ronda de trabajo de campo.
* Identificación de interesados y catálogo inicial de requisitos.
* Primeros diagramas de contexto y de casos de uso.

\---

## \[0.1.0] — 2026-05 — Entrega 1 (1A)

### Añadido

* Conformación del equipo, asignación de roles y plan de trabajo.
* Identificación del sistema real y del cliente.
* Elicitación inicial y aval institucional.
* Estructura base del repositorio.
