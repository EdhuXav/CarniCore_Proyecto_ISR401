> **Actualización — decisión final de destino (ver `CHANGELOG.md`, v2.1.0).**
> Este análisis, hecho el 02/08/2026, comparaba *Requirements Engineering*
> (Springer), *Journal of Systems and Software* (Elsevier) e *IEEE
> Transactions on Software Engineering*, y recomendaba priorizar la revista
> *Requirements Engineering*. Esa recomendación **quedó reemplazada**: el
> destino final elegido por el equipo es **REFSQ 2027, track Research**
> (15 páginas incl. referencias), reflejado en la cabecera de
> `manuscrito_final.tex` y en la plantilla `llncs.cls` que usa el
> manuscrito. El motivo del cambio (documentado en el CHANGELOG) es que el
> manuscrito corregido, con el trabajo relacionado ampliado, el análisis de
> sensibilidad y las ocho amenazas a la validez, no cabía en las 8 páginas
> de *Posters & Tools* de REFSQ, y el equipo decidió que un track de
> conferencia con revisión por pares era una meta más realista en el plazo
> del curso que un envío directo a un journal JCR. El resto de este
> documento se conserva como registro del análisis inicial, no como la
> decisión vigente.

# Análisis de revistas candidatas para publicación -- CarniCore (Enfoque 2)

**Carpeta:** `08_Publicacion/analisis_revistas.md`
**Fecha de la búsqueda:** 02/08/2026
**Fuentes:** sitios oficiales de cada editorial (Springer Link, ScienceDirect/Elsevier, IEEE Xplore) y SCImago Journal Rank (SJR), consultados en vivo el mismo día. Enlaces completos en la sección de Referencias.

## Resumen para el equipo

El estudio de CarniCore (Enfoque 2 -- detección automática de ambigüedad, diseño censal sobre 25 RF, panel reducido de personas expertas) es un **estudio de caso académico de alcance acotado**, no un estudio industrial a gran escala. Esto condiciona qué revistas son un destino realista: las candidatas de mayor prestigio en Ingeniería de Requisitos tienden a exigir muestras más grandes o validación industrial para un artículo completo. Se documentan igualmente como referencia, y se deja una recomendación de ruta más realista al final.

## Tabla comparativa

| Criterio | **Requirements Engineering** (Springer) | **Journal of Systems and Software** (Elsevier) | **IEEE Transactions on Software Engineering** (IEEE) |
|---|---|---|---|
| Editorial / modelo | Springer, híbrida (suscripción + acceso abierto opcional) | Elsevier, híbrida (suscripción + acceso abierto opcional) | IEEE, híbrida (suscripción + acceso abierto opcional) |
| Alcance declarado | Revista multidisciplinaria centrada en la elicitación, representación y validación de requisitos de sistemas intensivos en software; pide explícitamente que los artículos aborden las consecuencias prácticas de las ideas y cómo evaluarlas en la práctica [1] | Cubre todos los aspectos de la ingeniería de software; exige que todo artículo aporte evidencia que respalde sus afirmaciones, mediante estudios empíricos, simulación, pruebas formales u otro tipo de validación [2] | Busca resultados teóricos bien definidos y estudios empíricos con impacto potencial en la construcción, el análisis o la gestión de software [3] |
| Indexación / cuartil (SJR) | SJR 0,798 -- Q2 [1] | SJR 0,975 -- Q1 en Hardware and Architecture, Information Systems y Software [4] | Q1; factor de impacto 6,5 (2023) [5] |
| Costo de publicar en acceso abierto (APC) | No confirmado en esta búsqueda; Springer opera bajo modelo híbrido, se debe consultar el precio vigente al momento del envío | USD 3.670 (sin impuestos), con posible reducción según la política de acceso abierto de la institución del equipo [2] | USD 2.800 para envíos del año 2026, bajo el modelo híbrido de acceso abierto que IEEE introdujo en 2013 [6] |
| Publicar sin pagar APC | Sí, vía suscripción -- el equipo no paga si no elige la ruta de acceso abierto | Sí -- Elsevier indica expresamente que no hay cargo si no se elige acceso abierto; el artículo queda disponible solo para quienes tengan suscripción [2] | Sí, vía suscripción (acceso a través de IEEE Xplore) |
| Encaje con el estudio | Alto en tema (ambigüedad de requisitos); exigente en tamaño de muestra y validación industrial para un artículo completo | Alto en tema (acepta evidencia empírica de cualquier tipo, no solo industrial a gran escala) | Muy alto prestigio, pero históricamente exige mayor escala y rigor estadístico que un estudio con 25 RF y 3--5 personas expertas |
| Tipo de contribución recomendada para este estudio | *Short paper* / nota de investigación | *Short paper* / reporte de caso de estudio | No recomendado como primer destino para este tamaño de estudio |

## Notas de interpretación

- El "Estimated APC" que SCImago muestra junto al SJR de *Requirements Engineering* es una aproximación calculada por la propia plataforma a partir del prestigio de la revista, no una tarifa oficial confirmada por Springer. SCImago aclara expresamente que esa cifra es una estimación basada en la calidad de la revista y no el precio real [1]; por eso no se reporta un número aquí y queda pendiente confirmarlo directamente en Springer Link al momento del envío.
- El gasto global en cargos por publicación abierta entre las editoriales grandes (incluyendo Elsevier y Springer Nature) casi se triplicó entre 2019 y 2023 [7], lo que confirma que estas cifras cambian con frecuencia y deben reverificarse antes del envío real, no asumirse fijas desde este documento.
- Ruta de bajo costo si el equipo no cuenta con fondos para el cargo de publicación abierta: publicar en modalidad de suscripción (sin pagar) en cualquiera de las tres, y depositar el manuscrito en Zenodo como versión previa o posterior a la revisión por pares, según la política de auto-archivo de cada editorial (verificar en Sherpa/RoMEO antes del envío).

## Recomendación del equipo

Dado el tamaño real del estudio (diseño censal, 25 RF, panel de 3 a 5 personas expertas), la recomendación es **no apuntar directamente a la revista de mayor prestigio (IEEE TSE)** para esta primera publicación, sino:

1. Priorizar **Requirements Engineering (Springer)** como primera opción, en modalidad de *short paper* o nota de investigación, por su encaje temático directo y su tradición de publicar estudios de caso académicos de alcance acotado.
2. Mantener **Journal of Systems and Software (Elsevier)** como segunda opción, por su exigencia expresa de evidencia empírica de cualquier tipo, no únicamente industrial a gran escala.
3. Reservar **IEEE Transactions on Software Engineering** como objetivo de mediano plazo, condicionado a ampliar el estudio (más RF, más personas expertas, posible réplica en otro dominio) en una futura entrega o tesis.

## Pendiente de responsabilidad del equipo

Este análisis compara revistas y su encaje temático; **no reemplaza** la verificación de la convocatoria vigente, los plazos de envío y la política de datos abiertos de cada revista en la fecha real de envío del manuscrito, ya que esa información cambia con el tiempo.

## Referencias

[1] Requirements Engineering -- SCImago Journal Rank. https://www.scimagojr.com/journalsearch.php?q=18660&tip=sid&clean=0

[2] Journal of Systems and Software -- ScienceDirect (Elsevier). https://www.sciencedirect.com/journal/journal-of-systems-and-software

[3] IEEE Transactions on Software Engineering -- IEEE Xplore. https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32

[4] Journal of Systems and Software -- Resurchify (SJR y cuartiles). https://www.resurchify.com/impact/details/19309

[5] IEEE Transactions on Software Engineering -- Wikipedia (factor de impacto 2023, fuente secundaria a verificar contra Clarivate/JCR). https://en.wikipedia.org/wiki/IEEE_Transactions_on_Software_Engineering

[6] IEEE Transactions on Software Engineering -- Grokipedia (APC 2026, fuente secundaria a verificar contra IEEE Author Center antes del envío). https://grokipedia.com/page/ieee_transactions_on_software_engineering

[7] Estimating global article processing charges paid to six publishers for open access between 2019 and 2023. https://arxiv.org/pdf/2407.16551
