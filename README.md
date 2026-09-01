# CarniCore_Proyecto_ISR401 — Sistema Inteligente para la Gestión Integral de un Centro Cárnico

> **Proyecto Fin de Curso · Ingeniería de Requerimientos (ISR-401) · 4to Nivel · Paralelo A**  
> Universidad Técnica Estatal de Quevedo (UTEQ) · Carrera de Ingeniería de Software  
> **Entrega 4 (2B / Defensa Final)** — ERS/SRS v2.0 definitiva + Componente Empírico + Manuscrito

![Entrega](https://img.shields.io/badge/Entrega-4_(2B/Defensa_Final)-green)
![Licencia docs](https://img.shields.io/badge/Licencia_docs-CC_BY_4.0-blue)
![Licencia código](https://img.shields.io/badge/Licencia_código-MIT-blue)
![FAIR](https://img.shields.io/badge/FAIR_Assessment-100%25_(16%2F16)-brightgreen)

---

## Tabla de contenidos

1. [Resumen del sistema](#resumen-del-sistema)
2. [Equipo de trabajo](#equipo-de-trabajo)
3. [Estado del proyecto por entrega](#estado-del-proyecto-por-entrega)
4. [Estructura del repositorio](#estructura-del-repositorio)
5. [Entregables clave](#entregables-clave)
6. [Cómo reproducir el análisis empírico](#cómo-reproducir-el-análisis-empírico)
7. [Cómo ejecutar el MVP](#cómo-ejecutar-el-mvp)
8. [Depósito FAIR](#depósito-fair)
9. [Ética y protección de datos](#ética-y-protección-de-datos)
10. [Publicación objetivo](#publicación-objetivo)
11. [Checklist Entrega 4 (2B)](#checklist-entrega-4-2b)
12. [Licencias](#licencias)
13. [Cómo citar este repositorio](#cómo-citar-este-repositorio)

---

## Resumen del sistema

**CarniCore** digitaliza y da trazabilidad a los procesos operativos críticos de una distribuidora de productos cárnicos en Pucayacu, La Maná, Cotopaxi, actualmente gestionados de forma manual.

**Problema:** la gestión manual genera inconsistencias en trazabilidad animal, demoras en reportes regulatorios y pérdida de información entre faenamiento, refrigeración, despiece y despacho.

**Propuesta de valor:**
- Trazabilidad animal extremo a extremo (lote → canal → corte → cliente), con vista pública vía QR (RF-26)
- Cumplimiento de normativa sanitaria ecuatoriana y **LOPDP**
- Reportería gerencial filtrable por proveedor (RF-27) y por período
- Predicción de demanda (IA-01) y detección de anomalías de cadena de frío (IA-02)



---

## Equipo de trabajo

| N.° | Nombres completos | Cédula | Correo institucional | Rol | ORCID |
|---:|---|---:|---|---|---|
| 1 | **Castro Bajaña Ariel Omar** | 2350262305 | acastrob@uteq.edu.ec | Líder / Analista líder | [0009-0005-1575-8935](https://orcid.org/0009-0005-1575-8935) |
| 2 | **Gamarra Araujo Edhu Xavier** | 1208370633 | egamarraa@uteq.edu.ec | Técnico — Modelador UML | [0009-0001-8312-9656](https://orcid.org/0009-0001-8312-9656) |
| 3 | **Crespo Espinoza Kleber Obed** | 1315380244 | kcrespoe@uteq.edu.ec | Técnico — Elicitación de campo | [0009-0000-9145-1357](https://orcid.org/0009-0000-9145-1357) |
| 4 | **Quintero Gende Erick Jahir** | 1250575527 | equinterog@uteq.edu.ec | Técnico — Verificador de calidad | [0009-0000-6032-4179](https://orcid.org/0009-0000-6032-4179) |
| 5 | **Pérez Ruiz Carlos Andrés** | 0955713136 | cperezr3@uteq.edu.ec | Secretario / Documentador | [0009-0003-6741-9391](https://orcid.org/0009-0003-6741-9391) |

**Docente supervisor:** PhD. Guerrero Ulloa Gleiston Cicerón | **Período:** 2026–2027 PPA | **Corte Entrega 4:** semana 17, agosto 2026

---

## Estado del proyecto por entrega

| Entrega | Nombre | Semana | Estado |
|---|---|:---:|---|
| 1A | Conformación del equipo y plan de trabajo | 4 | ✅ Cerrada |
| 1B | ERS/SRS parcial + primera ronda de campo | 10 | ✅ Cerrada |
| 2A (= 3) | ERS/SRS completo + componente empírico | 13 | ✅ Cerrada |
| **2B / Defensa** | **ERS definitivo + manuscrito + defensa** | **17** | **✅ Entregada — depósito Zenodo publicado, FAIR 100%** |

---

## Estructura del repositorio

```
CarniCore_Proyecto_ISR401/
├── README.md                        ← este archivo (actualizado post-defensa)
├── LICENSE                          ← MIT (código) + CC BY 4.0 (datos/doc)
├── CITATION.cff                     ← v2.0.0 con ORCID, DOI Zenodo y SWHID reales
├── CHANGELOG.md                     ← historial desde 1A hasta 4 (2B) — última entrada v3.0.0
├── checksums.sha256                 ← ✅86 entradas; 
├── fair_assessment.pdf              ← ✅ Autoevaluación F-UJI/FAIR — 16/16 indicadores, 100%
│
├── 01_ERS/
│   ├── ERS_SRS_2B_v2.0.pdf         ← ✅ definitivo
│   ├── ERS_SRS_2B_v2.0.tex         ← ✅ definitivo
│   ├── figures/                    ← ✅ diagramas UML, mockups, consentimientos, actas escaneadas
│   └── referencias.bib             ← ✅ base bibliográfica del ERS
│
├── 02_Evidencias/
│   ├── 00_Restringido/             ← [R] AES-256, 16 contenedores .7z (uno por entrevista) + evaluadores independientes
│   │   └── fichas_tecnicas.csv     ← ✅ completo, con hashes SHA-256 reales por archivo
│   ├── Consentimientos/            ← ✅ 16/16 (ENTR-01 a ENTR-16)
│   ├── Transcripciones/            ← ✅ 16/16
│   ├── Fotos_Entorno/              ← ✅ 20/20
│   ├── Cuestionario/
│   │   ├── Fotos_Aplicacion/       ← ✅ 5 fotos
│   │   └── Respuestas/             ← ✅ CSV consolidado de la encuesta (90 respuestas, según fair_assessment.pdf)
│   ├── Documentos_Organizacion/    ← ⚠️ 3/5 (faltan 2 para el mínimo de la guía)
│   ├── Validacion_Walkthrough/     ← ✅ 5 actas técnicas/no técnicas + videos de evidencia
│   
│
├── 03_Modelado/                     ← ✅ UML completo (Contexto, Casos de Uso, Clases, Componentes, Despliegue, SD estratégico) + 20 Mockups + enlace Figma
├── 04_Trazabilidad/
│   ├── Matriz_Trazabilidad.csv     ← ✅ 60 filas (27 RF + 15 RNF + 18 IA)
│   └── priorizacion_moscow_kano.csv
│
├── 05_MVP/                          ← ✅ frontend (HTML/JS) + backend, video de demostración
│   ├── README.md
│   ├── video_demo.mp4
│   └── Ejecutable/CarniCore/
│
├── 06_Experimento/
│   ├── protocolo.pdf               ← ✅ Enfoque 2, registrado OSF
│   ├── osf_registration.pdf        ← ✅ https://osf.io/wud69
│
│   ├── instrumentos/               ← ✅ guión, cuestionario, consentimiento, rúbrica, panel de expertos
│   ├── datos_crudos/                ← ✅ plantillas de expertos anonimizadas
│   ├── datos_procesados/            ← ✅ etiquetas_expertos.csv
│   ├── prompts_llm/                ← ✅ 3 prompts documentados
│   ├── resultados/                 ← ✅ CSVs/JSON de kappa, matriz de confusión, bootstrap IC95
│   └── scripts_analisis/
│       ├── detector_ambiguedad.py  ← ✅ script principal
│       ├── 01_importar_datos.py … 04_bootstrap_ic95.py ← ✅ pipeline modular
│       ├── rf27.json / rf25.json   ← ✅ RF verbatim
│       ├── run_all.py              ← ✅ orquestador (reemplaza al run_all.sh original)
│       ├── Makefile                ← ✅ alternativa de orquestación
│       └── requirements.txt        ← ✅ dependencias
│
├── 07_Publicacion/
│   ├── manuscrito_final.pdf/.tex   ← ✅ formato estilo LNCS/Springer (para Requirements Engineering)
│   ├── referencias.bib / splncs04.bst ← ✅
│   ├── figuras/ · tablas/          ← ✅ generadas por los scripts
│   └── dataset_zenodo/
│       ├── README_dataset.md / ANONYMIZATION.md / ETHICS.md / LICENSE.txt ← ✅
│       └── (paquete .zip depositado directamente en Zenodo, DOI abajo)
│
├── 08_Etica/                        ← ✅ A01–A13 + Adenda_Segunda_Ronda + README_Etica
└── 09_Defensa/                      ← ✅ completa: presentación (.pdf/.pptx), guion, video_defensa.mp4, folleto de una hoja
```

---

## Entregables clave

| Recurso | Ubicación / Enlace |
|---|---|
| ERS/SRS v2.0 definitivo (PDF) | `01_ERS/ERS_SRS_2B_v2.0.pdf` |
| Protocolo experimental | `06_Experimento/protocolo.pdf` |
| Registro OSF | https://osf.io/wud69 |
| Scripts de análisis | `06_Experimento/scripts_analisis/` |
| MVP funcional | `05_MVP/` → `docker compose up -d` |
| Documentación ética | `08_Etica/` |
| Manuscrito final | `07_Publicacion/manuscrito_final.pdf` |
| Presentación de defensa | `09_Defensa/presentacion.pdf` / `.pptx` |
| **Dataset Zenodo (DOI)** | ✅ https://doi.org/10.5281/zenodo.22225854 |
| **SWHID Software Heritage** | ✅ `swh:1:dir:5741b167af89a201c815b061cc965309d8167069` (ver `CITATION.cff`) |

---

## Cómo reproducir el análisis empírico

```bash
# 1. Clonar
git clone https://github.com/EdhuXav/CarniCore_Proyecto_ISR401.git
cd CarniCore_Proyecto_ISR401

# 2. Verificar integridad multimedia
sha256sum -c checksums.sha256
# ⚠️ Nota: al 1-sep-2026 este archivo aún referencia rutas de una versión anterior
#    (01_ERS/main.tex, 01_ERS/figura/istar_SD.svg) y 5 archivos no coinciden en hash.
#    Pendiente regenerar checksums.sha256 contra el árbol actual antes de considerarlo verificado.

# 3. Instalar dependencias Python
python -m venv .venv && source .venv/bin/activate
pip install -r 06_Experimento/scripts_analisis/requirements.txt

# 4. Ejecutar pipeline completo
python 06_Experimento/scripts_analisis/run_all.py
# (alternativa equivalente: make -C 06_Experimento/scripts_analisis)

# Salidas relevantes en 06_Experimento/resultados/ y 07_Publicacion/figuras|tablas/:
#   clasificaciones_detector.csv
#   kappa_resultados.json, matriz_confusion_prf1.json, bootstrap_ic95.json
#   figura_01_distribucion_categorias.png / figura_02_estado_por_rf.png (Figs. del manuscrito)
#   tabla_01_resultados_detector.tex (Tabla del manuscrito)
```

---

## Cómo ejecutar el MVP

```bash
cd 05_MVP/Ejecutable/CarniCore
docker compose up -d
# Backend: http://localhost:4000
# pgAdmin: docker compose --profile tools up -d  →  http://localhost:5050

# Credenciales de demostración:
# Usuario admin: admin@carnicore.ec  /  carnicore_pass  (pgAdmin)
# API: POST /api/auth/login  →  ver seed.js para credenciales demo
```

**Escenarios de demostración trazados:**
1. **Escenario A — Ingreso y trazabilidad de lote** (cubre RF-01, RF-02, RF-03, RF-11): registrar proveedor → guía de origen → lote → consultar trazabilidad completa.
2. **Escenario B — Pesaje y vida útil** (cubre RF-04, RF-05, RF-07, RF-08): registrar pesaje → emitir comprobante → ingresar a cámara → verificar alerta de vida útil.

---

## Depósito FAIR

| Plataforma | URL | Estado |
|---|---|---|
| GitHub (repositorio) | https://github.com/EdhuXav/CarniCore_Proyecto_ISR401 | ✅ |
| OSF (protocolo) | https://osf.io/wud69 | ✅ |
| **Zenodo (dataset)** | **https://doi.org/10.5281/zenodo.22225854** (https://zenodo.org/records/22225854) | ✅ |
| **Software Heritage** | `swh:1:dir:5741b167af89a201c815b061cc965309d8167069` | ✅ |

**Autoevaluación FAIR (F-UJI / FAIR Data Maturity Model, RDA 2020):** `fair_assessment.pdf` — **16/16 indicadores cumplidos (100%)**, muy por encima del mínimo del 60% exigido por la guía ISR-401 §7.5 (Findable 5/5, Accessible 4/4, Interoperable 3/3, Reusable 4/4). Evaluado el 1 de septiembre de 2026 y supervisado por PhD. Guerrero Ulloa Gleiston Cicerón.

---

## Ética y protección de datos

- **Zona pública [P]:** transcripciones anonimizadas, consentimientos con cédula/firma enmascaradas, fotos sin rostros ni GPS, respuestas sin columnas identificativas.
- **Zona restringida [R]:** contenedor AES-256 en `02_Evidencias/00_Restringido/` — contraseña entregada al docente por SGA, nunca en el repositorio.
- **Nomenclatura multimedia:** `YYYY-MM-DD_TipoParticipante_ENTR-XX_Tecnica.ext`
- **Retención:** 24 meses desde cierre; dataset anonimizado en Zenodo indefinidamente (CC BY 4.0).

---

## Publicación objetivo

**Revista primaria:** Requirements Engineering (Springer, ISSN 0947-3602, JIF 3.3, Q2)  
**Alternativas:** REFSQ 2027 Posters & Tools (envío: 4 feb 2027); IST Elsevier (JIF 4.3, Q1)  
**Declaración al docente:** registrada por correo institucional en semana 14. Ver análisis comparativo completo en `07_Publicacion/analisis_revistas.md`.

---

## Checklist Entrega 4 (2B)

- [x] La estructura de carpetas coincide con la Sección 9.1 de la guía
- [x] `01_ERS/ERS_SRS_2B_v2.0.pdf` existe y está unificado
- [x] `08_Etica/` completo y vigente (A01–A13 + Adenda + README)
- [x] `02_Evidencias/00_Restringido/fichas_tecnicas.csv` existe con hashes reales
- [x] ≥16 consentimientos, ≥16 transcripciones (16/16 cada uno); videos/audios en `00_Restringido/`
- [ ] `02_Evidencias/Codificacion_Tematica/curva_saturacion.png` — **pendiente, carpeta vacía**
- [ ] `02_Evidencias/Member_Checking/` con acta de ≥3 participantes — **pendiente, carpeta no existe**
- [ ] `02_Evidencias/Documentos_Organizacion/` ≥5 documentos — **pendiente, hay 3/5**
- [x] El paquete Zenodo tiene DOI real en `CITATION.cff` y `README.md` (10.5281/zenodo.22225854)
- [x] SWHID de Software Heritage en `CITATION.cff`
- [x] `fair_assessment.pdf` con puntaje F-UJI/FAIR — 100% (16/16), supera el ≥60% requerido
- [x] El pipeline de análisis (`run_all.py` / `Makefile`) reproduce las tablas y figuras del manuscrito
- [x] El manuscrito está en plantilla tipo LNCS/Springer para la revista objetivo
- [x] `09_Defensa/` completa: presentación, guion, video, folleto
- [ ] `checksums.sha256` verifica sin error en clon limpio — **pendiente, 5 discrepancias y 2 rutas obsoletas (`main.tex`, `figura/istar_SD.svg`) que deben regenerarse**
- [ ] `06_Experimento/osf_deviations.pdf` — **pendiente, no está en el repo**
- [ ] Commits distribuidos entre los 5 integrantes con correos institucionales — verificar en `Insights → Contributors` de GitHub

---

## Licencias

| Material | Licencia |
|---|---|
| Código fuente del MVP | MIT |
| ERS/SRS y dataset anonimizado | CC BY 4.0 |
| `02_Evidencias/00_Restringido/` | Sin licencia — no se redistribuye |

---

## Cómo citar este repositorio

```bibtex
@software{carnicore_isr401_2026,
  author    = {Castro Bajaña, Ariel Omar and Gamarra Araujo, Edhu Xavier and
               Crespo Espinoza, Kleber Obed and Quintero Gende, Erick Jahir and
               Pérez Ruiz, Carlos Andrés},
  title     = {{CarniCore}: Detección automática de patrones de ambigüedad en requisitos
               funcionales — Paquete de replicación Entrega 4 (2B)},
  version   = {2.0.0},
  year      = {2026},
  doi       = {10.5281/zenodo.22225854},
  url       = {https://github.com/EdhuXav/CarniCore_Proyecto_ISR401}
}
```

---
*Última actualización: 1 de septiembre de 2026 · Quevedo, Ecuador — UTEQ · ISR-401 · 2026–2027 PPA*
