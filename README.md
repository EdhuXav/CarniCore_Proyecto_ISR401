# CarniCore_Proyecto_ISR401 — Sistema Inteligente para la Gestión Integral de un Centro Cárnico

> Proyecto Fin de Curso · Ingeniería de Requerimientos (ISR-401) · 4to Nivel · Paralelo A
> Universidad Técnica Estatal de Quevedo (UTEQ) · Carrera de Ingeniería de Software
> Entrega 3 (2A) — Especificación de Requisitos completa + Componente Empírico

Curso: ISR-401 · Nivel: 4to · Paralelo: A · Entrega: 3 (2A) · Licencia docs: CC BY 4.0 · Licencia código: MIT

---

## Tabla de contenidos

1. [Resumen del sistema](#resumen-del-sistema)
2. [Equipo de trabajo](#equipo-de-trabajo)
3. [Docente y asignatura](#docente-y-asignatura)
4. [Estado del proyecto por entrega](#estado-del-proyecto-por-entrega)
5. [Estructura del repositorio](#estructura-del-repositorio)
6. [Entregables clave (enlaces)](#entregables-clave-enlaces)
7. [Componente empírico — cómo reproducir el análisis](#componente-empírico--cómo-reproducir-el-análisis)
8. [Estándares y marco normativo](#estándares-y-marco-normativo)
9. [Ética y protección de datos](#ética-y-protección-de-datos)
10. [Publicación objetivo](#publicación-objetivo)
11. [Cómo ejecutar localmente](#cómo-ejecutar-localmente)
12. [Checklist de la rúbrica (autoverificación)](#checklist-de-la-rúbrica-autoverificación)
13. [Licencias](#licencias)
14. [Cómo citar este repositorio](#cómo-citar-este-repositorio)
15. [Contacto](#contacto)

---

## Resumen del sistema

**CarniCore** es un sistema de software diseñado para la **gestión integral de un centro cárnico** (faenamiento, trazabilidad, inventario, ventas y reportes sanitarios), construido sobre un levantamiento de requisitos con evidencia empírica recogida en dos rondas de trabajo de campo con los stakeholders del dominio.

**Problema que aborda:** la gestión manual o con sistemas aislados en centros cárnicos genera inconsistencias en trazabilidad animal, demoras en reportes regulatorios y pérdida de información entre las áreas de faenamiento, refrigeración, despiece y despacho. CarniCore unifica esos procesos en una sola plataforma verificable.

**Propuesta de valor:**
- Trazabilidad animal de extremo a extremo (lote → canal → corte → cliente).
- Cumplimiento de la normativa sanitaria ecuatoriana y de la **LOPDP** (Ley Orgánica de Protección de Datos Personales).
- Reportería regulatoria y operativa en tiempo real.
- Componente basado en IA con requisito de explicabilidad como RNF (Chazette & Schneider, 2020).

> Aviso sobre generación con IA: ninguna parte de este ERS, ni de los resultados del componente empírico, es producto de un LLM sin respaldo empírico verificable. Toda afirmación sustantiva está anclada a una evidencia primaria (entrevista, cuestionario, foto, documento) o a una referencia bibliográfica revisada por pares. Esta restricción es de cumplimiento obligatorio (rúbrica — gatekeeper G4).

---

## Equipo de trabajo

**Nómina del equipo estudiantil · Paralelo A · 4to nivel · ISR-401**

| N.° | Nombres completos | Cédula | Matrícula | Paralelo | Correo institucional | Rol asignado |
|---:|---|---:|---:|:---:|---|---|
| 1 | **Castro Bajaña Ariel Omar** | 235026205 | 616630 | A | acastrob@uteq.edu.ec | Líder / Analista líder |
| 2 | **Gamarra Araujo Edhu Xavier** | 1208370633 | 616369 | A | egamarraa@uteq.edu.ec | Técnico — Modelador UML |
| 3 | **Crespo Espinoza Kleber Obed** | 1315380244 | 616968 | A | kcrespoe@uteq.edu.ec | Técnico — Apoyo en elicitación de campo |
| 4 | **Quintero Gende Erick Jahir** | 1250575527 | 617126 | A | equinterog@uteq.edu.ec | Técnico — Verificador de calidad |
| 5 | **Pérez Ruiz Carlos Andrés** | 0955713136 | 616557 | A | cperezr3@uteq.edu.ec | Secretario / Documentador |

### Responsabilidades por rol

- **Líder / Analista líder** — conducción del equipo, elicitación, redacción del ERS y firma del entregable.
- **Técnico — Modelador UML** — modelado del sistema, diagramas CU/clases/secuencia/estados/componentes/despliegue.
- **Técnico — Apoyo en elicitación de campo** — logística y aplicación de entrevistas, cuestionarios y walkthroughs.
- **Técnico — Verificador de calidad** — revisión de requisitos (atributos, métricas, ambigüedad, cobertura).
- **Secretario / Documentador** — versionado del repositorio, `CHANGELOG.md`, `CITATION.cff`, anonimización de evidencias.

---

## Docente y asignatura

| | |
|---|---|
| **Docente responsable** | Ing. **Guerrero Ulloa Gleiston Cicerón** |
| **Asignatura** | Ingeniería de Requerimientos (ISR-401) |
| **Carrera** | Ingeniería de Software (Rediseño) |
| **Universidad** | Universidad Técnica Estatal de Quevedo (UTEQ) |
| **Periodo académico** | 2026–2027 PPA |
| **Corte de la Entrega 3 (2A)** | miércoles 29 de julio de 2026, 00:00 (último commit válido) |

---

## Estado del proyecto por entrega

| Entrega | Nombre | Semana | Estado | Carpeta principal |
|---|---|:---:|---|---|
| 1A | Conformación del equipo y plan de trabajo | 4 | Cerrada | `01_ERS/` (anterior) |
| 1B | ERS/SRS parcial + primera ronda de campo | 10 | Cerrada | `02_Evidencias/` (ronda 1) |
| **2A** | **ERS/SRS completo + componente empírico** | **13** | **En curso** | `01_ERS/`, `06_Experimento/` |
| 2B / Defensa | Manuscrito paralelo + envío a revista JCR | 17 | Pendiente | `07_Publicacion/` |

---

## Estructura del repositorio

El árbol es **obligatorio** y debe coincidir exactamente con la Sección 8.1 de la rúbrica. Nombres en ASCII, sin acentos ni espacios; palabras separadas con guion bajo.

```
CarniCore_Proyecto_ISR401/
├── README.md                       <- este archivo
├── LICENSE                         <- MIT (código) + CC BY 4.0 (datos/doc)
├── CITATION.cff                    <- formato Citation File Format v1.2.0
├── CHANGELOG.md                    <- historial desde 1A hasta la fecha
├── .gitignore
├── checksums.sha256                <- SHA-256 de todos los archivos multimedia
│
├── 01_ERS/                         <- Especificación de Requisitos de Software
│   ├── ERS_SRS_2A_v1.0.pdf
│   ├── ERS_SRS_2A_v1.0.tex
│   └── referencias.bib
│
├── 02_Evidencias/                  <- Trabajo de campo (zonas [P] y [R])
│   ├── 00_Restringido/             <- [R] contenedor AES-256 (7Z / VeraCrypt)
│   │   ├── evidencias_restringidas.7z
│   │   └── fichas_tecnicas.csv
│   ├── Consentimientos/            <- [P] copias enmascaradas (JPG/PDF)
│   ├── Transcripciones/            <- [P] TXT / JSON anonimizadas
│   ├── Fotos_Entorno/              <- [P] JPG sin GPS ni rostros
│   ├── Cuestionario/
│   │   ├── Fotos_Aplicacion/       <- [P] JPG
│   │   └── Respuestas/             <- [P] CSV / XLSX sin columnas identificativas
│   ├── Documentos_Organizacion/    <- [P] PDFs anonimizados
│   ├── Validacion_Walkthrough/     <- [P] actas enmascaradas
│   └── Codificacion_Tematica/      <- [P] CSV
│
├── 03_Modelado/
│   ├── Diagramas_UML/              <- .xmi / .puml / .qea + PNG 300 dpi + SVG
│   └── Mockups/                    <- PNG + enlace Figma
│
├── 04_Trazabilidad/
│   ├── matriz_trazabilidad.csv     <- >= 40 filas
│   └── priorizacion_moscow_kano.csv
│
├── 05_MVP/                         <- Producto Minimo Viable
│   ├── README.md                   <- despliegue + cobertura RF Must
│   └── video_demo.mp4              <- <= 3 min
│
├── 06_Experimento/                 <- Componente empirico
│   ├── protocolo.pdf               <- PICOC + hipotesis + plan estadistico
│   ├── osf_registration.pdf        <- registro previo en osf.io
│   ├── instrumentos/               <- guiones v2.0, cuestionario v2.0, rubrica
│   ├── prompts_llm/                <- prompts con modelo, temp, top-p, seed
│   ├── resultados/                 <- CSV crudos y procesados, figuras
│   └── scripts_analisis/           <- R / Python reproducibles
│
├── 07_Publicacion/                 <- Puente a Entrega 4 (2B)
│   ├── manuscrito_borrador.pdf
│   ├── analisis_revistas.md        <- candidatas APC + suscripcion
│   └── dataset_zenodo/             <- paquete para Zenodo (CC BY 4.0) - PENDIENTE
│       ├── README_dataset.md
│       └── (archivos del dataset)
│
└── 08_Etica/                       <- Paquete etico (gatekeeper G8)
    ├── A01_Protocolo_Investigacion.pdf
    ├── A02_Instrumentos_Recoleccion.pdf
    ├── ... (A.01 a A.13)
    ├── Categoria_A/ | _B/ | _C/   <- segun riesgo del proyecto
    ├── Adenda_Segunda_Ronda.pdf    <- semana 11, antes del primer consentimiento nuevo
    └── README_Etica.md
```

---

## Entregables clave (enlaces)

| Recurso | Ubicación / Enlace |
|---|---|
| ERS/SRS completo (PDF unificado) | `01_ERS/ERS_SRS_2A_v1.0.pdf` |
| Diagramas UML | `03_Modelado/Diagramas_UML/` |
| Mockups | `03_Modelado/Mockups/` |
| Matriz de trazabilidad (>= 40 filas) | `04_Trazabilidad/matriz_trazabilidad.csv` |
| MVP funcional (dentro del repo) | `05_MVP/` |
| Video demo del MVP (<= 3 min) | `05_MVP/video_demo.mp4` |
| Protocolo experimental (PDF) | `06_Experimento/protocolo.pdf` |
| Registro OSF del protocolo | `06_Experimento/osf_registration.pdf` (con URL persistente https://osf.io/...) |
| Scripts de análisis | `06_Experimento/scripts_analisis/` |
| Dataset en Zenodo (DOI) | `07_Publicacion/dataset_zenodo/` → Zenodo |
| Documentación ética | `08_Etica/` |

> Nota sobre el MVP: este proyecto aloja el Producto Mínimo Viable **dentro del mismo repositorio**, en la carpeta `05_MVP/`. No se usa un repositorio Git separado.

---

## Componente empírico — cómo reproducir el análisis

Esta sección describe cómo reproducir el estudio empírico que sustenta los resultados del ERS y el manuscrito paralelo. Sigue el flujo exigido por la rúbrica (Sección 5 de la guía).

### Enfoque elegido

- [x] **Enfoque 2** — Detectar automáticamente ambigüedad y *smells* en los requisitos (Ferrari et al., 2016; Fischbach et al., 2023).

*(Enfoque declarado en `08_Etica/Adenda_Segunda_Ronda.pdf` y registrado en OSF antes del inicio de la recolección.)*

### Pregunta de investigación (formato PICOC)

La pregunta de investigación se hereda sin modificaciones de la Sección 7.1 del ERS/SRS y de la Sección 3 de la Adenda Ética de la Segunda Ronda, para mantener trazabilidad completa entre ambos documentos.

**RQ1.** ¿Con qué precisión un detector automático replica el juicio de personas expertas al identificar RF ambiguos en el conjunto de requisitos de CarniCore?

**RQ2.** ¿Cuál es el acuerdo inter-evaluador (κ de Cohen / κ de Fleiss) entre las personas expertas al clasificar los mismos RF como ambiguos o no ambiguos?

**RQ3.** ¿Qué tipos de *smells* de requisitos (cuantificadores vagos, conjunciones múltiples, voz pasiva) concentran la mayor cantidad de desacuerdos entre el detector y los expertos?

### Componentes del PICOC

| Elemento | Descripción |
|---|---|
| **P** — Población | Conjunto de requisitos funcionales (RF) elicitados para CarniCore, alineados a la Sección 3.3 del ERS (mínimo 25). |
| **I** — Intervención | Detector automático (herramienta tipo *smella* de Ferrari et al., o script propio en Python con regex para cuantificadores vagos, conjunciones múltiples y voz pasiva). |
| **C** — Comparación | Juicio consensuado de ≥ 3 personas evaluadoras independientes (5 recomendado) que clasifican cada RF como "ambiguo" o "no ambiguo" sin ver la salida del detector. |
| **O** — Resultado | Precisión, exhaustividad (*recall*), medida F1 del detector respecto al consenso experto; acuerdo inter-evaluador (κ de Cohen por pares, κ de Fleiss global); tamaño del efecto y potencia estadística. |
| **C** — Contexto | Sistema de software real del dominio cárnico ecuatoriano, con RF producidos por el propio equipo en la Entrega 2 (1B) y refinados en la Entrega 3 (2A). |

### Reproducibilidad paso a paso

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/EdhuXav/CarniCore_Proyecto_ISR401.git
   cd CarniCore_Proyecto_ISR401
   ```

2. **Verificar integridad de las evidencias**
   ```bash
   sha256sum -c checksums.sha256
   ```
   Cada hash debe coincidir con el archivo multimedia declarado en `02_Evidencias/00_Restringido/fichas_tecnicas.csv`.

3. **Verificar la zona restringida (con contraseña entregada al docente por el SGA)**
   ```bash
   cd 02_Evidencias/00_Restringido
   7z x evidencias_restringidas.7z      # o abrir con VeraCrypt
   cd ../..
   ```

4. **Instalar dependencias del análisis**
   ```bash
   # Opción Python
   python -m venv .venv && source .venv/bin/activate
   pip install -r 06_Experimento/scripts_analisis/requirements.txt

   # Opción R
   Rscript -e "renv::restore('06_Experimento/scripts_analisis/')"
   ```

5. **Ejecutar el pipeline de análisis**
   ```bash
   # Datos crudos -> datos procesados -> tablas -> figuras
   bash 06_Experimento/scripts_analisis/run_all.sh
   ```
   Los scripts reproducen **exactamente** las tablas y figuras del manuscrito a partir de los datos crudos (no se aceptan tablas producidas a mano).

6. **Contrastar con el manuscrito**
   Abrir `07_Publicacion/manuscrito_borrador.pdf` y comparar las tablas/figuras generadas con las del documento. Cualquier discrepancia debe explicarse en la sección *Amenazas a la validez*.

### Pasos del Enfoque 2 (resumen operativo)

1. Seleccionar el detector (herramienta existente o script Python con regex para cuantificadores vagos, conjunciones múltiples y voz pasiva).
2. Ejecutar el detector sobre el conjunto completo de RF del ERS (mínimo 25, según la Sección 3.3) y clasificar cada uno como "ambiguo" o "no ambiguo".
3. Entregar los RF a ≥ 3 personas expertas (5 recomendado) y pedirles la misma clasificación, sin que vean la salida del detector.
4. Calcular **precisión**, **exhaustividad** y **F1** del detector tomando como referencia el consenso experto.
5. Calcular el acuerdo inter-evaluador **κ de Cohen** (por pares) y **κ de Fleiss** (global).
6. Discutir los desacuerdos: para cada RF donde expertos y detector no coinciden, redactar una breve nota con la razón del desacuerdo y la lección aprendida.

### Variables de entorno opcionales
```bash
export OSF_TOKEN="..."        # solo para subir resultados a OSF (no necesario para reproducir)
export ZENODO_TOKEN="..."     # solo para depositar dataset (semana 16)
```

---

## Estándares y marco normativo

| Estándar / marco | Uso en el proyecto |
|---|---|
| **ISO/IEC/IEEE 29148:2018** | Procesos del ciclo de vida e ingeniería de requisitos. |
| **ISO/IEC 25010:2023** | Modelo de calidad del producto: 9 características para los RNF. |
| **Pohl (2010)** | Fundamentos de Ingeniería de Requerimientos. |
| **SWEBOK v4.0** (Washizaki, 2024) | Cuerpo de conocimiento de IS. |
| **MoSCoW** (Clegg, 1994) | Priorización Must / Should / Could / Won't. |
| **Modelo de Kano** (1984) | Clasificación básicas / desempeño / deleite. |
| **WSJF** (SAFe) | Valor de negocio = costo-de-retraso / duración. |
| **UML 2.5** (OMG) | Modelado del sistema. |
| **INVEST** (Wake, 2003) | Calidad de historias de usuario. |
| **Connextra** (2001) | Plantilla de historia de usuario. |
| **Gherkin** | Escenarios Dado-Cuando-Entonces. |
| **PICOC** | Preguntas de investigación del estudio empírico. |
| **κ de Cohen / Fleiss** | Acuerdo inter-evaluador. |
| **Cohen d / Cliff δ** | Tamaño del efecto. |
| **Principios FAIR** (Wilkinson, 2016) | Gestión del dataset publicado. |
| **LOPDP Ecuador** (Reg. Of. 459, 2021) | Ley Orgánica de Protección de Datos Personales. |
| **Citation File Format v1.2.0** | `CITATION.cff` de este repositorio. |
| **Keep a Changelog** | `CHANGELOG.md` de este repositorio. |

### Marco ético
Cumplimiento simultáneo de esta guía y del **Paquete Integral de Anexos y Guías de Elaboración — Solicitud de Aprobación Ética (ISR-401, 2026–2027 PPA)**. Toda la documentación ética vive en `08_Etica/`. La vigencia de ese paquete es condición de admisión (gatekeeper **G8**).

---

## Ética y protección de datos

- **Zona pública [P]:** accesible directamente en el repo (transcripciones anonimizadas, consentimientos con cédula/firma enmascaradas, fotos sin rostros ni GPS, respuestas sin columnas identificativas).
- **Zona restringida [R]:** consentimientos originales, videos/audios sin anonimizar, actas firmadas y documentos originales del cliente. Se almacenan en `02_Evidencias/00_Restringido/` como contenedor cifrado **AES-256** (7Z o VeraCrypt). La contraseña se entrega **únicamente al docente** por el espacio de la actividad en el SGA — **nunca** dentro del repo ni del README.
- **Nomenclatura de archivos:** `YYYY-MM-DD_TipoParticipante_CodigoParticipante_Tecnica.ext` (p. ej. `2026-09-05_Veterinario_ENTR-03_Entrevista.mp4`). Se usa el código de participante, nunca el nombre propio.
- **Identificables prohibidos en la zona pública:** firma, cédula, rostro, voz, coordenadas GPS.
- **Retención:** los datos crudos restringidos se conservan **24 meses** desde el cierre del proyecto y luego se eliminan con acta firmada. El dataset anonimizado en Zenodo se conserva **indefinidamente** bajo CC BY 4.0.
- **Anonimización del cliente:** en artefactos públicos y en el manuscrito, la organización aparece con el seudónimo declarado en su protocolo de anonimización (depositado en `08_Etica/`). Su identidad real solo es verificable mediante el aval institucional para el docente (gatekeeper **G3**).

---

## Publicación objetivo

El equipo apunta a un **artículo completo** (full research paper) en una revista indexada en **JCR** del área de Ingeniería de Requerimientos, de las editoriales **Springer Nature**, **Elsevier** o **IEEE**, seleccionada en la semana 16 con las herramientas oficiales de cada editorial (ver `07_Publicacion/analisis_revistas.md`).

**Herramientas oficiales para búsqueda de revista:**
- **Springer Nature** → journalsuggester.springer.com
- **Elsevier** → journalfinder.elsevier.com
- **IEEE** → publication-recommender.ieee.org

**Búsqueda en modalidad mixta (requisito):** el archivo `07_Publicacion/analisis_revistas.md` debe contener al menos **dos candidatas de cada editorial** (una con APC y una por suscripción o híbrida sin cargo), evaluando: nombre, indexación JCR + cuartil, factor de impacto, modelo de acceso, APC en USD, tiempo medio a primera decisión, tasa de aceptación, ajuste temático.

---

## Cómo ejecutar localmente

### Requisitos previos
- Git ≥ 2.30
- Python ≥ 3.10 *o* R ≥ 4.2
- 7-Zip o VeraCrypt (para la zona restringida)
- `ffprobe` y `sha256sum` (verificación de evidencias)
- LaTeX (para regenerar el ERS desde el `.tex`)

### Pasos
```bash
# 1. Clonar
git clone https://github.com/EdhuXav/CarniCore_Proyecto_ISR401.git
cd CarniCore_Proyecto_ISR401

# 2. Verificar integridad multimedia
sha256sum -c checksums.sha256

# 3. (Opcional) Regenerar el ERS PDF desde LaTeX
cd 01_ERS
latexmk -pdf ERS_SRS_2A_v1.0.tex
cd ..

# 4. Desplegar el MVP (dentro del mismo repo, en 05_MVP/)
cd 05_MVP
docker compose up -d          # o seguir las instrucciones de 05_MVP/README.md
```

---

## Checklist de la rúbrica (autoverificación)

Lista de chequeo del equipo (también usada por el docente como filtro preliminar de gatekeepers). Se debe actualizar antes del corte.

- [ ] La estructura de carpetas coincide **exactamente** con la Sección 8.1 (incluida `08_Etica/`).
- [ ] Existen los **5 archivos raíz obligatorios**: `README.md`, `LICENSE`, `CITATION.cff`, `CHANGELOG.md`, `checksums.sha256`.
- [ ] El PDF del ERS/SRS está unificado, numerado, con historial de versiones y enlace al repo en la portada.
- [ ] `08_Etica/` está completo (paquete base + adenda de la segunda ronda con fecha anterior al primer consentimiento nuevo).
- [ ] El contenedor `02_Evidencias/00_Restringido/` abre con la contraseña entregada al docente y coincide con `fichas_tecnicas.csv`.
- [ ] Todos los archivos multimedia siguen la nomenclatura `YYYY-MM-DD_Tipo_Codigo_Tecnica.ext`.
- [ ] Cada audio/video pasa `ffprobe` sin error y tiene duración > 0.
- [ ] Cada consentimiento de la zona pública tiene cédula y firma enmascaradas; el original íntegro está en el contenedor cifrado.
- [ ] Ninguna fotografía publicada conserva GPS ni rostros identificables.
- [ ] El cuestionario tiene fotos de aplicación y respuestas con **n >= 30** por perfil dominante (o censo justificado + potencia).
- [ ] El protocolo experimental está **registrado en OSF** con fecha anterior a la ejecución (guardado en `06_Experimento/osf_registration.pdf`).
- [ ] Los prompts LLM (si aplica) incluyen modelo, temperatura, top-p, top-k, semilla y fecha.
- [ ] Los scripts de análisis reproducen las tablas y figuras del manuscrito a partir de los datos crudos.
- [ ] El hash SHA-256 de cada archivo multimedia está en `checksums.sha256` y coincide en el corte.
- [ ] La matriz de trazabilidad tiene **>= 40 filas** con todas las columnas obligatorias.
- [ ] Todas las evidencias declaradas en el ERS existen dentro del repo y son verificables.

**Gatekeepers a cuidar especialmente en esta entrega:** G1 (enlace al SGA), G3 (aval ético), G4 (evidencia real), G5 (mínimos cuantitativos), G8 (paquete ético).

---

## Licencias

Este repositorio aplica **dos licencias coexistentes**, declaradas de forma expresa en `LICENSE`:

| Material | Licencia | Alcance |
|---|---|---|
| Código fuente del MVP | **MIT** o **Apache-2.0** | Uso, modificación y redistribución con atribución. |
| Documento ERS/SRS y dataset anonimizado | **Creative Commons Atribución 4.0 Internacional (CC BY 4.0)** | Reutilización con citación adecuada. |
| Material en `02_Evidencias/00_Restringido/` | **Sin licencia — no se redistribuye** | Datos personales identificables; permanecen bajo custodia del docente. |

---

## Cómo citar este repositorio

Usa el botón **"Cite this repository"** de GitHub o el archivo `CITATION.cff` (formato Citation File Format v1.2.0). Ejemplo en BibTeX:

```bibtex
@software{carnicore_isr401_2026,
  author    = {Castro Bajaña, Ariel Omar and
               Gamarra Araujo, Edhu Xavier and
               Crespo Espinoza, Kleber Obed and
               Quintero Gende, Erick Jahir and
               Pérez Ruiz, Carlos Andrés},
  title     = {{CarniCore}: Sistema Inteligente para la Gestión Integral de un Centro Cárnico},
  version   = {2A-v1.0},
  year      = {2026},
  date      = {2026-07-29},
  publisher = {Universidad Técnica Estatal de Quevedo},
  doi       = {<!-- TODO: pegar DOI de Zenodo -->},
  url       = {https://github.com/EdhuXav/CarniCore_Proyecto_ISR401}
}
```

---

## Contacto

| Rol | Persona | Correo |
|---|---|---|
| Líder / Analista líder | Castro Bajaña Ariel Omar | acastrob@uteq.edu.ec |

---

Última actualización: 2026 · Quevedo, Ecuador — UTEQ · ISR-401 · 2026–2027 PPA
