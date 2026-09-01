# 08_Etica/ — Documentación ética del proyecto CarniCore

## Categoría de riesgo

Este estudio opera bajo **categoría de riesgo C (riesgo mínimo operativo)**, según
lo declarado en el ERS/SRS v2.0 (`01_ERS/ERS_SRS_2B_v2.0.tex`, sección
"Consideraciones éticas"). No se recolectan datos personales identificables más
allá de un código de participante; la información sensible (nombres, firmas,
contacto) se resguarda en la zona `[R]` restringida del repositorio
(`02_Evidencias/00_Restringido/`), nunca en texto plano en carpetas públicas.

## Estructura de esta carpeta

```
08_Etica/
├── A01_Protocolo_Investigacion.pdf
├── A02_Instrumentos_Recoleccion.pdf
├── A03_Consentimiento_Informado.pdf
├── A04_Plan_Gestion_Datos.pdf
├── A05_Aval_Institucional.pdf
├── A06_Declaracion_Conflicto_Intereses.pdf
├── A07_Compromiso_Confidencialidad.pdf
├── A08_CV_Docente.pdf
├── A09_Nomina_Equipo.pdf
├── A10_Cronograma_Gantt.pdf
├── A11_Analisis_Riesgos.pdf
├── A12_Certificado_Etica.pdf
├── A13_Participantes_Externos.pdf
├── Categoria_C/                  <- documentación específica de la categoría de
│                                    riesgo C asignada al proyecto (ver más abajo)
├── Adenda_Segunda_Ronda.pdf       <- adenda posterior a la primera revisión del
│                                    comité, con fecha anterior al inicio de la
│                                    recolección de datos de la segunda ronda
└── README_Etica.md                <- este archivo
```

**Nota sobre jerarquía:** `Adenda_Segunda_Ronda.pdf` es un documento de proceso
(registra una segunda ronda de revisión del protocolo) y vive al mismo nivel que
`Categoria_C/`, no dentro de ella. `Categoria_C/` contiene la documentación propia
de la clasificación de riesgo del proyecto; la adenda es un evento posterior y
distinto en el ciclo de revisión ética, por lo que ambas carpetas son hermanas,
no una anidada en la otra.

## Qué contiene cada anexo (paquete base A01–A13)

| Anexo | Contenido |
|---|---|
| A01 | Protocolo de investigación completo |
| A02 | Instrumentos de recolección de datos (guías de entrevista, cuestionarios) |
| A03 | Formato de consentimiento informado firmado por los participantes |
| A04 | Plan de gestión de datos (almacenamiento, retención, destrucción) |
| A05 | Aval institucional de la UTEQ |
| A06 | Declaración de conflicto de intereses del equipo |
| A07 | Compromiso de confidencialidad firmado por el equipo investigador |
| A08 | CV del docente supervisor |
| A09 | Nómina del equipo de investigación |
| A10 | Cronograma Gantt del componente ético/empírico |
| A11 | Análisis de riesgos del estudio |
| A12 | Certificado de aprobación ética |
| A13 | Documentación de participantes externos (panel de expertos, entrevistados) |

## Alcance de esta documentación

Esta carpeta cubre la ética del **proceso de investigación** (entrevistas de
elicitación, walkthroughs de validación, panel de expertos para RQ1). No
duplica ni reemplaza:

- La declaración de uso de herramientas de IA generativa en el desarrollo del
  proyecto, que reside en el ERS/SRS (apéndice correspondiente) y pendiente de
  trasladar también al manuscrito final.
- La anonimización específica del panel de expertos de RQ1, documentada en
  `06_Experimento/datos_crudos/README.md` y `06_Experimento/datos_procesados/`.
- Los consentimientos y transcripciones de las entrevistas de campo, en
  `02_Evidencias/Consentimientos/` y `02_Evidencias/Transcripciones/`.

## Estado de esta carpeta

Paquete A01–A13 y Adenda de Segunda Ronda completos. Pendiente: crear la
subcarpeta `Categoria_C/` con la documentación de clasificación de riesgo
correspondiente, si el comité de ética la exige como entregable separado del
resto del paquete base.
