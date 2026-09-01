# README — Paquete de Replicación CarniCore
**Título:** Replication package for "Detección automática de patrones de ambigüedad en requisitos funcionales: un estudio exploratorio en el dominio de trazabilidad cárnica"

**DOI:** 10.5281/zenodo.22225854 
**OSF:** https://osf.io/wud69  
**Repositorio GitHub:** https://github.com/EdhuXav/CarniCore_Proyecto_ISR401  
**Licencia datos:** Creative Commons Atribución 4.0 Internacional (CC BY 4.0)  
**Licencia código:** MIT  
**Fecha:** agosto de 2026

---

## Autores

| Nombre | ORCID | Institución |
|--------|-------|-------------|
| Castro Bajaña, Ariel Omar | 0009-0005-1575-8935 | UTEQ |
| Crespo Espinoza, Kleber Obed | 0009-0000-9145-1357 | UTEQ |
| Gamarra Araujo, Edhu Xavier | 0009-0001-8312-9656 | UTEQ |
| Pérez Ruiz, Carlos Andrés | 0009-0003-6741-9391 | UTEQ |
| Quintero Gende, Erick Jahir | 0009-0000-6032-4179 | UTEQ |

---

## Descripción del estudio

Este paquete contiene todos los materiales necesarios para replicar el estudio:

**RQ1:** ¿Con qué precisión un detector automático replica el juicio de personas expertas al identificar RF ambiguos en el conjunto de requisitos de CarniCore?

El estudio aplica un detector automático de ambigüedad léxico-sintáctica (cuantificadores vagos, conjunciones múltiples, voz pasiva sin agente explícito) sobre los 27 requisitos funcionales del sistema CarniCore, comparando los resultados con el consenso de un panel de expertos.

**Enfoque metodológico:** Enfoque 2 — Detección automática de ambigüedad (Fischbach et al., 2023; Ferrari et al., 2016)  
**Contexto:** Sistema de distribución cárnica en Ecuador, dominio no explorado previamente en la literatura de ambigüedad de requisitos.

---

## Contenido del paquete

```
README_dataset.md              ← este archivo
ANONYMIZATION.md               ← procedimiento de anonimización aplicado
ETHICS.md                      ← principios éticos y LOPDP
LICENSE.txt                    ← CC BY 4.0 para datos, MIT para código

datos/
  rf27.json                    ← 27 RF verbatim del ERS/SRS v2.0 (anonimizados)
  clasificaciones_detector.csv ← salida real del detector sobre los 27 RF
  datos_crudos.csv             ← clasificaciones por RF (raw)
  datos_procesados.csv         ← resultado del análisis de consistencia

  [cuando haya panel experto:]
  juicios_expertos.csv         ← clasificaciones de cada evaluador por RF
  consenso_experto.csv         ← consenso calculado (mayoría simple)

scripts/
  detector_ambiguedad.py       ← detector automático (Python, regex)
  analisis_kappa_f1.py         ← cálculo de kappa y F1 [PENDIENTE panel experto]
  run_all.sh                   ← orquestador: reproduce tablas y figuras

instrumentos/
  guion_entrevista_v2.0.pdf   ← guión de las entrevistas de elicitación
  rubrica_evaluacion_experta.pdf ← rúbrica para el panel de expertos
  02_cuestionario_v2.0.pdf    ← cuestionario aplicado a stakeholders

transcripciones/
  [transcripciones anonimizadas en formato Markdown/TXT]
  [seudónimos sustituyen nombres reales]

respuestas_cuestionario/
  encuesta_respuestas.csv     ← respuestas sin columnas identificativas
```

---

## Diccionario de datos

### rf27.json
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | string | Identificador del RF (RF-01 a RF-27) |
| descripcion | string | Texto verbatim del RF del ERS/SRS v2.0 |
| prioridad | string | MoSCoW (Must/Should/Could/Won't) |

### clasificaciones_detector.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_rf | string | Identificador del RF |
| ambiguo_detector | int | 1=ambiguo detectado, 0=no ambiguo |
| categorias_activadas | string | Categorías que activaron el flag |
| evidencia_cuantificador_vago | string | Términos vagos encontrados |
| evidencia_conjuncion_multiple | string | Conectores contados |
| evidencia_voz_pasiva | string | Construcción pasiva encontrada |

### datos_procesados.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID | string | Identificador del RF |
| Estado | string | Correcto / Mejorable |
| Duplicado | string | Si/No |
| Inconsistente | string | Si/No |
| Conflicto | string | Si/No |
| Ambiguo | string | Si/No (según detector) |

---

## Cómo reproducir el análisis

```bash
# 1. Clonar el repositorio
git clone https://github.com/EdhuXav/CarniCore_Proyecto_ISR401.git
cd CarniCore_Proyecto_ISR401

# 2. Instalar dependencias
pip install -r 06_Experimento/scripts_analisis/requirements.txt

# 3. Ejecutar pipeline completo
bash 06_Experimento/scripts_analisis/run_all.sh

# 4. Los resultados se generan en:
#    06_Experimento/resultados/
```

---

## Citación

Si usa este paquete, cítelo como:

```
Castro Bajaña A.O., Crespo Espinoza K.O., Gamarra Araujo E.X., Pérez Ruiz C.A., Quintero Gende E.J. (2026).
Replication package for "Detección automática de patrones de ambigüedad en requisitos funcionales: 
un estudio exploratorio en el dominio de trazabilidad cárnica".
Zenodo. https://doi.org/10.5281/zenodo.22225854
```

Siguiendo los principios de citación de software de Smith, Katz y Niemeyer (2016).
