# ANONYMIZATION.md — Procedimiento de Seudonimización y Anonimización
**Proyecto:** CarniCore — ISR-401, UTEQ 2026-2027 PPA  
**Aplicado en:** agosto de 2026

---

## Principios aplicados

La anonimización se realizó siguiendo:
1. Los principios de minimización y seudonimización de la Ley Orgánica de Protección de Datos Personales (LOPDP) del Ecuador (Registro Oficial Suplemento 459, 2021).
2. Las guías de investigación reproducible de Wilkinson et al. (2016) — principios FAIR.
3. Las directrices del Paquete Integral de Anexos y Guías de Elaboración ISR-401, 2026-2027 PPA.

---

## Categorías de datos y tratamiento

### Datos identificables — Zona Restringida [R]
Almacenados en `02_Evidencias/00_Restringido/` como contenedor cifrado AES-256:

| Dato | Tratamiento |
|------|-------------|
| Nombre y apellido del participante | Sustituido por código de participante (ENTR-01 a ENTR-XX) |
| Número de cédula | Eliminado de toda zona pública |
| Firma manuscrita | Cubierta en copias públicas |
| Voz (grabaciones originales) | Cifrada en zona restringida; solo audios originales |
| Rostro (videos originales) | Cifrado en zona restringida; sin videos en zona pública |
| Coordenadas GPS en fotografías | Eliminadas via exiftool antes de publicar en zona [P] |
| RUC/datos fiscales de la organización | Eliminados; organización referenciada como "distribuidora cárnica" |

### Datos anonimizados — Zona Pública [P]

| Dato | Tratamiento aplicado |
|------|---------------------|
| Transcripciones de entrevistas | Nombres propios → seudónimo (ej. "la propietaria", "el carnicero"); códigos de participante visibles |
| Consentimientos en zona pública | Cédula y firma cubiertas; código de participante visible |
| Fotografías del entorno | Seleccionadas sin rostros ni coordenadas GPS |
| Respuestas de cuestionario | Sin columnas de nombre, correo, teléfono, IP ni dirección |
| Nombre de la organización | Referenciada como "Distribuidora Cárnicos Pucayacu" (seudónimo acordado con la cliente) |

---

## Procedimiento de seudonimización de transcripciones

1. Leer transcripción completa
2. Identificar todos los nombres propios de personas
3. Sustituir por el código de participante (ENTR-01, ENTR-02, etc.) o por el rol (ej. "la Propietaria")
4. Identificar nombres de proveedores o clientes mencionados
5. Sustituir por genéricos (ej. "un proveedor de Quevedo")
6. Verificar que no queden cédulas, teléfonos, correos ni direcciones exactas
7. Guardar el archivo en `02_Evidencias/Transcripciones/` con nomenclatura `YYYY-MM-DD_TipoParticipante_ENTR-XX_Transcripcion.txt`

---

## Verificación

La organización cliente ha dado su consentimiento explícito para:
- La publicación de datos anonimizados en Zenodo bajo CC BY 4.0
- El uso de sus datos en publicaciones científicas revisadas por pares

Este consentimiento está documentado en los formularios A03 de la carpeta `09_Etica/`.

---

## Datos NO publicados en este paquete

Los siguientes datos permanecen bajo custodia del docente en la zona restringida:
- Grabaciones de audio y video originales
- Consentimientos informados originales con firma y cédula
- Datos que permitan identificar individualmente a los participantes
- Documentos originales de la organización con membrete/RUC
