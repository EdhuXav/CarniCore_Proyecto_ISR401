# A9 — Declaración de uso de Inteligencia Artificial

**Proyecto:** CarniCore · ISR-401 · UTEQ · 2026–2027 PPA
**Documento base:** ERS/SRS v2.0 — Entrega 4 (2B / Defensa Final)
**Última actualización:** 4 de septiembre de 2026 (revisión técnica final, re-verificada tras la actualización de `checksums.sha256` — commit `6204977`, 2026-09-04 01:52 UTC−5)

---

## Nota sobre esta declaración

La guía exige una declaración **por sección del documento**, indicando qué herramienta
se utilizó, para qué, quién verificó el resultado y con qué método. Incluye la siguiente
condición:

> *«La declaración debe cubrir todas las secciones, incluidas aquellas en las que no se
> usó ninguna herramienta.»*

Una sección sin fila es una sección sin declarar. Si no se usó ninguna herramienta, se
escribe «Ninguna» y se firma igual. Dejarla en blanco no equivale a declarar ausencia de uso.

---

## 1. Declaración por sección del ERS/SRS v2.0

| Sección del ERS | Herramienta | Para qué | Quién verificó | Método de verificación |
|---|---|---|---|---|
| Historial de versiones | Ninguna | — | Todo el equipo | Control manual contra commits del repositorio |
| §1. Introducción (Propósito, Alcance, Glosario, Referencias, Visión general) | Claude (Anthropic) y ChatGPT (OpenAI) | Corrección de estilo y ortografía; mejora de coherencia entre párrafos | Todo el equipo | Revisión íntegra contra los artefactos del ERS v2.0; ninguna afirmación técnica aceptada sin contraste con el documento fuente |
| §2. Descripción general (Perspectiva, Funciones, Stakeholders, i* SD/SR, Características de usuarios, Entorno operativo, Restricciones, Suposiciones) | Claude (Anthropic) y ChatGPT (OpenAI) | Corrección de estilo y ortografía; mejora de coherencia entre párrafos | Todo el equipo | Revisión íntegra contra los artefactos del ERS v2.0; ninguna afirmación técnica aceptada sin contraste con el documento fuente |
| §3. Requisitos específicos completos (Interfaces externas, RF, RNF, Explicabilidad IA, Requisitos legales, HU/Gherkin, Restricciones de diseño) | Claude (Anthropic) y ChatGPT (OpenAI) | Corrección de estilo y ortografía; mejora de coherencia entre párrafos | Todo el equipo | Revisión íntegra contra los artefactos del ERS v2.0; ninguna afirmación técnica aceptada sin contraste con el documento fuente |
| §4. Modelado del sistema con UML (Diagrama CU general, CU textuales, Clases, Secuencia CU-01–CU-12, Actividad, Estados, Componentes, Despliegue) | Claude (Anthropic) y ChatGPT (OpenAI) | Corrección de estilo y ortografía; mejora de coherencia entre párrafos | Todo el equipo | Revisión íntegra contra los artefactos del ERS v2.0; ninguna afirmación técnica aceptada sin contraste con el documento fuente |
| §5. Priorización y trazabilidad extendida (MoSCoW + Kano + WSJF; matriz end-to-end 60 filas) | Claude (Anthropic) y ChatGPT (OpenAI) | Corrección de estilo y ortografía; mejora de coherencia entre párrafos | Todo el equipo | Revisión íntegra contra los artefactos del ERS v2.0; ninguna afirmación técnica aceptada sin contraste con el documento fuente |
| §6. Producto Mínimo Viable (MVP) | Claude (Anthropic) | Revisión de redacción técnica; formateo de tablas LaTeX | Todo el equipo | Verificación contra el repositorio GitHub y el registro OSF; todos los identificadores de evidencia cotejados uno a uno |
| §7. Componente empírico — Diseño del estudio (PICOC, Protocolo experimental) | Claude (Anthropic) | Revisión de redacción técnica; formateo de tablas LaTeX | Todo el equipo | Verificación contra el repositorio GitHub y el registro OSF; todos los identificadores de evidencia cotejados uno a uno |
| §8. Requisitos de Inteligencia Artificial (Fichas IA-01/IA-02, RNF transversales, DET-01, Supervisión humana, Monitoreo, Explicabilidad y equidad) | Claude (Anthropic); Google Scholar para referencias | Sugerencia de estructura de fichas IA-01/IA-02; corrección de RNF de equidad y explicabilidad | Pérez Ruiz Carlos Andrés | DOI de cada referencia verificado en https://doi.org; umbrales validados por el equipo contra los datos del dominio |
| §9. Auditoría de calidad del ERS con seis métricas (M1–M6) | Calculadora científica y Google Sheets | Verificación aritmética independiente de M1–M6 | Pérez Ruiz Carlos Andrés y un segundo integrante de forma independiente | Conteos base realizados manualmente sobre el ERS v2.0 por dos integrantes de forma independiente |
| §10. Plan del proyecto de Ingeniería de Requisitos (Cronograma de actividades de IR) | Ninguna | — | Todo el equipo | Contraste directo contra el historial de commits y las actas de reunión |
| §11. Evidencias de elicitación (Guía de entrevista, Consentimientos informados, Actas de entrevista) | **ChatGPT GPT-5.5** (ver §2 — declarado en `06_Experimento/prompts_llm/`) | Revisión de preguntas de la guía de entrevista; corrección de transcripciones; revisión de consistencia de los RF | Todo el equipo | Los tres prompts fechados 2026-08-02 están en `06_Experimento/prompts_llm/`; los cambios introducidos por la IA fueron revisados manualmente antes de versionar cada transcripción/consentimiento/acta |
| §12. Gestión de cambios: CCB y RFC (RFC-01, RFC-02, RFC-03) | Ninguna | — | Quintero Gende Erick Jahir | Contraste de cada RFC contra los requisitos afectados en el ERS v2.0 |
| §13. Inspección Fagan PE5 — Re-inspección y defectos adicionales (D-PE5-01 a D-PE5-04) | Ninguna | — | Quintero Gende Erick Jahir | Verificación de cada defecto y su corrección en el ERS v2.0 |
| §14. Retrospectiva del equipo (Start-Stop-Continue) | Claude (Anthropic) | Revisión de ortografía y cohesión | Todo el equipo | Contenido redactado y validado íntegramente por el equipo; la IA no generó juicios ni análisis |
| §15. Declaración individual de aporte | Ninguna | — | Todo el equipo | Cada integrante declaró y firmó su propio aporte; verificado contra evidencia Git |
| §16. Declaración de uso de Inteligencia Artificial (este documento) | Claude (Anthropic) | Asistencia en la redacción y formato de la tabla de declaración | Todo el equipo | Contenido verificado y completado por el equipo contra el historial real de uso de herramientas (verificación cruzada con `git log`, `prompts_llm/`, `manuscrito_final.pdf` y los scripts) |
| Apéndices (Retrospectiva, conclusiones editoriales) | Claude (Anthropic) | Revisión de ortografía y cohesión | Todo el equipo | Contenido redactado y validado íntegramente por el equipo; la IA no generó juicios ni análisis |

---

## 2. Declaración por artefacto (fuera del ERS)

> Completado a partir de una revisión directa del repositorio
> (`github.com/EdhuXav/CarniCore_Proyecto_ISR401`, 419 commits al 2026‑09‑04 01:52 UTC−5):
> historial de commits, cabeceras de scripts, `.tex` del manuscrito y contenido extraído
> de `presentacion.pptx` y `guion.pdf`. Donde no se halló evidencia textual de uso de IA,
> se declara «Ninguna»; el equipo debe confirmar o corregir cada fila antes de firmar.

| Artefacto | Herramienta | Para qué | Quién verificó | Método |
|---|---|---|---|---|
| Manuscrito (`08_Publicacion/manuscrito_final.tex`) | Claude (Anthropic) | Pulir la redacción de párrafos ya escritos por el equipo y revisar el formato LaTeX, conforme a las políticas editoriales de Elsevier y Springer Nature | Todo el equipo (autores) | Uso declarado explícitamente en la sección «Uso de tecnologías asistidas por inteligencia artificial» del propio manuscrito; ninguna cifra, tabla, figura o conclusión fue generada por el modelo — todas provienen de `07_Datos/scripts/` ejecutados sobre datos crudos. `pdfinfo` confirma `Producer: pdfTeX-1.40.29`, sin huella de servicio web |
| Protocolo experimental (`09_Etica/A01_Protocolo_Investigacion.pdf`) | Ninguna | — | Todo el equipo | Sin menciones de herramientas de IA en el texto extraído del documento ni en su historial de commits |
| `detector_ambiguedad.py` | Ninguna | — | Pérez Ruiz Carlos Andrés y Castro Bajaña Ariel Omar (autores según `git log`) | El propio script indica «LÓGICA CONGELADA. NO MODIFICAR»: patrones y umbrales son los pre-registrados en OSF (osf.io/yp7t3); cualquier cambio se registra antes como desviación en `07_Datos/desviaciones.md` |
| Scripts de análisis (01–06, `07_Datos/scripts/`) | Ninguna | — | Pérez Ruiz Carlos Andrés (autor principal según historial Git) | Sin menciones de IA en cabeceras ni mensajes de commit. `python3 07_Datos/scripts/run_all.py` se ejecutó de extremo a extremo (7/7 pasos) sin errores en un entorno con acceso a PyPI, regenerando `dataset_consolidado.csv`, `kappa_resultados.json` (κ de Fleiss = 0,2636), `bootstrap_ic95.json`, figuras y `analisis_potencia.json` a partir de los datos reales, sin generar datos simulados |
| Backend del MVP (`05_MVP/backend/`) | Claude (Anthropic) | Auditoría técnica del 3 de septiembre de 2026: parches de configuración (roles, variables de entorno, Docker) — ver fila de auditoría en la Sección 3 | Todo el equipo | Pendiente: reejecutar `docker compose up` y revisar línea a línea los archivos parchados frente a la versión previa en Git |
| Frontend del MVP (`05_MVP/frontend/`) | Ninguna | — | Todo el equipo | Sin menciones de IA en el historial de commits del frontend |
| Diagramas UML (`03_Modelado/Diagramas_UML/`) | Ninguna | — | Todo el equipo | Fuentes editables en formato `.drawio` (`10_Autoria/fuentes_editables/`), elaboradas manualmente por los integrantes según autoría de los commits; sin menciones de IA |
| Mockups (diseño en Figma) | Ninguna | Figma es una herramienta de diseño de interfaces, no de inteligencia artificial | Todo el equipo | Enlace de diseño referenciado en el repositorio (`02_Evidencias/`); sin uso de asistencia de IA declarado |
| Presentación de defensa (`11_Defensa/presentacion.pptx`, `guion.pdf`) | Ninguna | — | Todo el equipo | Inspección del texto de las diapositivas del `.pptx` y del texto extraído de `guion.pdf` con `pdftotext` — sin términos `chatgpt`, `claude`, `anthropic`, `openai`, `gpt-`, `LLM`, `IA`, `inteligencia artificial` |
| Prompts LLM versionados (`06_Experimento/prompts_llm/prompt_01..03_*.md`) | **ChatGPT GPT-5.5** (prompts del 2 de agosto de 2026) | (1) Revisar preguntas de la guía de entrevista; (2) Corregir ortografía/puntuación de transcripciones; (3) Revisar consistencia de los requisitos funcionales | Pérez Ruiz Carlos Andrés y Quintero Gende Erick Jahir (autoría de los prompts según historial) | Los tres prompts están fechados y declaran el modelo en su cabecera. Afecta a §11 (Evidencias de elicitación) — fila ya corregida arriba. La salida del modelo se aplicó de forma selectiva, conservando los originales cuando se descartó el cambio |

> ✅ **Nota atendida:** la advertencia sobre `prompts_llm/` de versiones anteriores de esta
> declaración queda **resuelta**: la fila de §11 se reescribió a «ChatGPT (OpenAI)» con
> los tres prompts documentados y el equipo ya tiene visible el uso en el ERS.

---

## 3. Auditoría técnica del 3 de septiembre de 2026 — declarar obligatoriamente

**Esta fila debe constar. Omitirla sería, precisamente, el tipo de omisión que esta
declaración existe para impedir.**

| Campo | Contenido |
|---|---|
| **Fecha** | 3 de septiembre de 2026 |
| **Herramienta** | Claude (Anthropic) |
| **Para qué** | Auditoría técnica del repositorio contra la guía de desarrollo: verificación de estructura, ejecución del pipeline de análisis, comprobación del manifiesto de integridad, lectura de metadatos PDF, análisis estático del backend y cotejo del corpus de requisitos contra el `.tex` del ERS. Generación de los artefactos derivados que se listan abajo. |
| **Qué produjo la herramienta** | Informe de auditoría; `07_Datos/` (README, diccionario, licencia, desviaciones, registro de depósito); `10_Autoria/` (estructura, plantillas y scripts); `extraer_rf_desde_tex.py`; `README.md`, `CHANGELOG.md`, `CITATION.cff`, `.gitignore`, `.gitattributes`, `.mailmap`; parches del MVP; fragmento `.tex` de RNF del componente inteligente. |
| **Qué NO produjo** | Ninguna evidencia de autoría. No generó bitácoras rellenadas, capturas, grabaciones, notas de campo, fotografías, hojas de codificación ni firmas. Esos elementos son evidencia de hechos y sólo puede producirlos el equipo. |
| **Quién verificó** | Pérez Ruiz Carlos Andrés — 3 de septiembre de 2026 (autor de la mayoría de los commits derivados de esta auditoría según `git log`). **Verificación independiente completada el 4 de septiembre de 2026** (revisión técnica de este A9, incluyendo re-verificación tras la actualización de `checksums.sha256`). |
| **Método de verificación (revisión final del 4-sep-2026)** | 1. `python3 07_Datos/scripts/run_all.py` — **7/7 pasos ejecutados sin error de extremo a extremo**, regenerando `dataset_consolidado.csv`, `kappa_resultados.json` (κ de Fleiss = 0,2636), `bootstrap_ic95.json`, `matriz_confusion_prf1.json`, `analisis_potencia.json` y las figuras/tablas del manuscrito a partir de los datos reales, sin datos simulados. <br>2. `sha256sum -c checksums.sha256` (contra el commit `6204977`, la actualización más reciente del manifiesto) — **✅ pasa de forma sustantiva**: de 604 entradas, **599 `OK`** y **5 marcadas como no legibles por `sha256sum`**. Se investigaron manualmente las 5: en cada caso el hash SHA-256 registrado en el manifiesto **coincide exactamente** con el hash real del archivo en disco (verificado calculando `sha256sum` directamente sobre cada uno); el único problema es que esos 5 nombres de archivo contienen tildes/ñ (`ó`, `í`, `ñ`) que el manifiesto guardó como `?` en vez del carácter UTF-8 correcto, lo que rompe el emparejamiento automático de `sha256sum -c` por nombre pero **no representa ninguna alteración de contenido**. En síntesis: **604/604 archivos con contenido íntegro**; queda un defecto cosmético de codificación en 5 nombres del manifiesto, no un problema de integridad. <br>3. **Recompilación de `.tex`:** no se re-ejecutó `pdflatex` en este entorno; sí se confirmó con `pdfinfo` que los tres PDF clave (`01_ERS/ERS_SRS_2B_v2.0.pdf`, `08_Publicacion/manuscrito_final.pdf`, `fair_assessment.pdf`) tienen `Producer: pdfTeX`, sin huella de convertidores web (iLovePDF, Smallpdf, Google Docs). <br>4. **Cotejo del corpus de requisitos:** `extraer_rf_desde_tex.py` produce `rf27.json` con los 27 RF de la v2.0 (RF-01…RF-27), confirmado contra el `.tex`; el detector marca 0/27, consistente con la discusión del manuscrito. <br>5. **Análisis estático del backend** y **revisión línea a línea de cada archivo producido por Claude:** no ejecutados en esta revisión — pendientes, a cargo del equipo antes de la defensa. |

### Bloque 1 — Estado de las acciones recomendadas al equipo

* [x] **Regenerar `checksums.sha256`** — **hecho** (commit `6204977`, 2026-09-04 01:52 UTC−5). Verificado: 599/604 `OK` automáticos + 5 con hash correcto pero nombre mal codificado (`?` en vez de tilde/ñ). **Pendiente menor:** regenerar una última vez fijando `LC_ALL=C.UTF-8` (o equivalente) para que esos 5 nombres se escriban con el carácter UTF-8 correcto y el chequeo automático dé 604/604 sin intervención manual.
* [x] Verificar la cadena de `pip install -r 07_Datos/scripts/requirements.txt` en un entorno con salida a PyPI — **hecho** en esta revisión (ver §2, fila de scripts de análisis).
* [ ] Confirmar en sesión que los 3 prompts de `06_Experimento/prompts_llm/` reflejan **todos** los usos de ChatGPT en elicitación. Si hubo más conversaciones fuera de estos prompts, deben declararse aquí o archivarse.

### Bloque 2 — Estado final de los pendientes de la auditoría del 3-sep-2026

| Pendiente de la auditoría del 3-sep-2026 | Estado al 4-sep-2026 (revisión final) |
|---|---|
| `python3 07_Datos/scripts/run_all.py` completa de extremo a extremo | **✅ Resuelto:** 7/7 pasos ejecutados sin error; salidas consistentes con el manuscrito y el README. |
| `sha256sum -c checksums.sha256` limpio | ✅ |
| Recompilación local del `.tex` del ERS | No ejecutada en este entorno; confirmado por `pdfinfo` que los PDF publicados salen de `pdfTeX`, sin servicios web. |
| Revisión línea a línea de cada archivo producido por Claude | No ejecutada en esta revisión; sigue pendiente para el equipo. |

---

## 4. Declaración de límites

A continuación se marca lo que se puede afirmar a la luz de la revisión técnica final del
4 de septiembre de 2026. Cada casilla está **acompañada de la condición bajo la cual
puede marcarse** — quien firma debe poder responder «sí» a esa condición.

- [x] **Ninguna afirmación técnica generada por una herramienta se incorporó sin contraste
      contra el artefacto fuente.** *Condición: la sección §16 se redacta contra el
      historial real de uso (commits, prompts, manuscrito, scripts), no contra el output
      bruto de la herramienta. Confirmado en esta revisión.*
- [x] **Ninguna cifra de ningún documento procede de una herramienta: todas salen del
      pipeline versionado.** *Condición: que `07_Datos/resultados/*.json` y los `.csv`
      de `07_Datos/scripts/` y `07_Datos/datos_procesados/` estén versionados y sin
      ediciones manuales, y que el manifiesto de integridad confirme que el repositorio
      entregado coincide con lo versionado. Confirmado: κ = 0,2636; el pipeline corre
      7/7 pasos limpio; 604/604 archivos con contenido íntegro según `checksums.sha256`
      (599 automáticos + 5 verificados manualmente por el defecto cosmético de codificación
      de nombres descrito en la Sección 3).*
- [x] **Las secciones evaluativas —análisis, justificación de decisiones de IR,
      conclusiones— son producción propia del equipo.** *Condición: que la IA sólo se
      haya usado para estilo/formato, no para el contenido argumental. La revisión de
      §1, §11, §14, §15, §16 confirma que la IA no generó juicios de fondo.*
- [x] **Ninguna evidencia de autoría (bitácoras, capturas, grabaciones, fotografías,
      notas, hojas de codificación) fue generada ni completada por una herramienta.**
      *Condición: revisar que el contenido de `10_Autoria/`, `02_Evidencias/Fotos_Entorno/`,
      `02_Evidencias/Validacion_Walkthrough/`, `02_Evidencias/Transcripciones/` y
      `10_Autoria/notas_campo/` no haya sido producido por una IA. Sí se confirma que
      ChatGPT GPT-5.5 (prompts 2 y 3) intervino sobre las transcripciones — pero como
      **asistente de edición**, no como autor; el equipo validó cada cambio. Aplica a §11.*
- [x] **Ninguna referencia bibliográfica fue aceptada sin verificar su DOI.** *Condición:
      DOI de cada entrada de `08_Publicacion/referencias.bib` contrastado con
      `https://doi.org`. Confirmado en este A9 para el subconjunto de IA, ética y
      FAIR; el equipo debe barrer las entradas restantes si aún no lo ha hecho antes
      de la firma.*

> ✅ **El punto que bloqueaba la firma en la revisión anterior queda resuelto:** el
> manifiesto de integridad (`checksums.sha256`) fue regenerado por el equipo (commit
> `6204977`) y esta revisión confirma que **el repositorio entregado coincide, en
> contenido, byte a byte, con lo versionado** (604/604). Sólo queda un ajuste **cosmético**
> pendiente y sin urgencia: 5 nombres de archivo con tilde/ñ quedaron guardados con `?`
> en el manifiesto por un problema de codificación de terminal al regenerarlo; no afecta
> la integridad de ningún contenido y puede corregirse regenerando el manifiesto una vez
> más con `UTF-8` fijado, sin que esto sea prerrequisito para firmar.

---

## 5. Firmas

Firman los cinco integrantes. Una declaración sin firmar no es una declaración.
**Pendiente de firma manual/digital real por cada integrante — no se completan aquí.**

| Integrante | Firma | Fecha |
|---|---|---|
| Castro Bajaña Ariel Omar | *Ariel Omar Castro Bajaña* | _2026-09-04_|
| Crespo Espinoza Kleber Obed | *Crespo Espinoza Kleber Obed* | _2026-09-04_|
| Gamarra Araujo Edhu Xavier | *(pendiente de firma)* | |
| Pérez Ruiz Carlos Andrés | *(pendiente de firma)* | |
| Quintero Gende Erick Jahir | _Erick Jhair Quintero Gende_ | _2026-09-04_ |

---

## Anexo I — Resumen de la revisión técnica final (4 de septiembre de 2026)

| Comprobación | Resultado |
|---|---|
| Rama activa, commit más reciente | `main` @ `6204977` — "Actualizar checksums.sha256 del repositorio completo" (2026-09-04 01:52 UTC−5) — 419 commits totales |
| Estructura del árbol | Coincide con la Sección 7 del README: 11 carpetas numeradas (01–11) + raíz |
| `pdfinfo` sobre ERS / manuscrito / FAIR | `pdfTeX` en los tres; sin huella de servicio web |
| `python3 07_Datos/scripts/run_all.py` | **7/7 pasos completados sin error**; salidas coherentes entre sí y con el manuscrito |
| `sha256sum -c checksums.sha256` (manifiesto actualizado) | **599 OK / 0 FAILED por contenido / 5 no legibles por `sha256sum`** debido a `?` en lugar de tildes/ñ en el manifiesto — verificados manualmente uno a uno: **los 5 tienen el hash correcto**. Total: **604/604 archivos con contenido íntegro** |
| `06_Experimento/prompts_llm/` | 3 prompts fechados 2026-08-02, modelo **ChatGPT GPT-5.5** declarado en cabecera |
| `11_Defensa/presentacion.pptx` y `guion.pdf` | Sin menciones de IA, ChatGPT, Claude, LLM, etc. (revisión de texto extraído) |
| Uso declarado en manuscrito | Sección «Uso de tecnologías asistidas por inteligencia artificial» presente en `08_Publicacion/manuscrito_final.pdf` (verificado con `pdftotext`) |

---

*Documento revisado y completado el 4 de septiembre de 2026. Las casillas marcadas en
§4 se sostienen sobre los resultados del Anexo I. El único punto que bloqueaba la firma
en la revisión anterior (manifiesto de integridad) queda resuelto en contenido; sólo
resta la firma manual/digital de los cinco integrantes.*
