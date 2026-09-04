# Libro de códigos — Doble codificación de requisitos funcionales (RF-01 a RF-27)

## 1. Propósito y unidad de análisis

Este libro de códigos define el criterio de clasificación que deben aplicar,
**de forma independiente y sin consultarse**, las dos personas codificadoras del
proceso de doble codificación (A7). La unidad de análisis es cada requisito
funcional (RF-01 a RF-27), representado por su campo `objetivo_referencia`.

El propósito del libro es que dos personas distintas, leyéndolo por separado,
lleguen a la misma decisión el mayor número de veces posible **por aplicar el
mismo criterio**, no por haberse puesto de acuerdo de antemano. El grado en que
esto ocurre es precisamente lo que mide `calcular_acuerdo.py` (acuerdo bruto, κ
de Cohen, IC 95% por bootstrap).

## 2. Esquema de códigos

| Código | Nombre | N.º esperado de RF |
|---|---|---|
| RT | Registro_transaccional | ~11 |
| TA | Trazabilidad_auditoría | ~5 |
| RA | Reportes_analítica | ~5 |
| GC | Gestión_configuración | 2 |
| CC | Continuidad_contingencia | 3 |

Cada RF recibe **un único código**. No se permiten códigos compuestos ni
categorías fuera de este listado.

## 3. Definiciones operacionales

### RT — Registro_transaccional
**Definición:** el requisito captura o emite un registro asociado a un evento
operativo puntual del negocio.
**Regla de inclusión:** verbo "registrar" o "emitir" + objeto = evento que
ocurre en un momento determinado (ingreso, pesaje, despiece, venta, devolución,
baja, movimiento).
**Regla de exclusión:** si el objeto es un parámetro persistente del sistema
(precio, rol) en lugar de un evento puntual, no es RT.
**Ejemplos ancla:** RF-01 "Registrar proveedor"; RF-04 "Registrar pesaje de
producto"; RF-10 "Registrar venta o salida de producto".

### TA — Trazabilidad_auditoría
**Definición:** el requisito reconstruye el recorrido de un producto o expone
evidencia verificable a un tercero.
**Regla de inclusión:** genera, consulta o exporta un vínculo que conecta el
producto con su historial u origen (código de lote, QR, evidencia de
auditoría).
**Regla de exclusión:** si lo consultado es una métrica agregada de negocio y
no el recorrido de una unidad de producto, no es TA (es RA).
**Ejemplos ancla:** RF-11 "Consultar trazabilidad de producto"; RF-25 "Generar
código QR de trazabilidad".

### RA — Reportes_analítica
**Definición:** el requisito produce una vista, reporte o filtro agregado sobre
datos ya existentes, sin capturar un evento nuevo ni reconstruir un recorrido.
**Regla de inclusión:** verbos "generar reporte", "visualizar panel",
"consultar historial [de precios]", "filtrar", "contar".
**Regla de exclusión:** si el verbo "consultar" tiene como objeto el recorrido
de un producto puntual, no es RA (es TA).
**Ejemplos ancla:** RF-13 "Generar reportes de ventas, compras y pérdidas";
RF-14 "Visualizar panel resumen del negocio".

### GC — Gestión_configuración
**Definición:** el requisito administra parámetros del sistema o del acceso,
no eventos de negocio.
**Regla de inclusión:** define quién opera el sistema o bajo qué parámetros
persistentes (roles, precios por tipo/temporada).
**Regla de exclusión:** si describe una transacción puntual aunque tenga tono
administrativo, no es GC (es RT).
**Ejemplos ancla:** RF-15 "Gestionar usuarios y roles"; RF-19 "Configurar
precios por tipo de producto y temporada".

### CC — Continuidad_contingencia
**Definición:** el requisito sostiene la operación ante fallas o alerta sobre
riesgo de pérdida o degradación del producto.
**Regla de inclusión:** modo offline, incidentes de infraestructura, alertas
automáticas de riesgo.
**Regla de exclusión:** un incidente comercial normal (ej. una devolución) no
es CC; es RT.
**Ejemplos ancla:** RF-20 "Registrar incidentes de corte de energía"; RF-21
"Operar en modo de contingencia offline".

## 4. Procedimiento de decisión (aplicar en orden)

1. Identifique el **objeto principal** de la acción del requisito: ¿es un
   evento a persistir, un vínculo de recorrido, una métrica agregada, un
   parámetro de sistema, o una amenaza a la continuidad operativa?
2. Asigne el código cuya definición coincide con ese objeto principal.
3. Si dos lecturas parecen igualmente válidas, resuelva por esta prioridad
   (de más específica a más genérica):

   ```
   TA > CC > RT > RA > GC
   ```

4. Registre su decisión sin revisarla contra la de la otra persona
   codificadora hasta que ambas hojas estén completas.

## 5. Casos límite documentados

El libro reconoce explícitamente 5 RF donde la aplicación del criterio admite
más de una lectura razonable. Se documentan aquí para que la persona
codificadora sepa que la discrepancia en estos puntos es un resultado válido
del proceso, no un error:

| RF | Tensión | Lectura por prioridad TA>CC>RT>RA>GC |
|---|---|---|
| RF-05 | Emitir comprobante de pesaje — RT vs. TA | RT (certifica un evento, no reconstruye recorrido) |
| RF-08 | Calcular y alertar vida útil — CC vs. RA | CC (la alerta de riesgo prima sobre el cálculo) |
| RF-16 | Registrar movimientos por fecha — RT vs. RA | RT (registra el evento, no solo lo consulta) |
| RF-17 | Registrar georreferencia — RT vs. TA | RT (el objeto es una coordenada puntual, no un vínculo de recorrido) |
| RF-22 | Registrar devoluciones — RT vs. CC | RT (evento comercial normal, no falla de sistema) |

## 6. Formato de entrega esperado por unidad codificadora

- Archivo: `hoja_codificador_<usuario>.csv`
- Columnas: `id`, `codigo`, `objetivo_referencia` (no modificar `id` ni
  `objetivo_referencia`).
- Valores válidos de `codigo`: exactamente `RT`, `TA`, `RA`, `GC`, `CC`
  (respetar mayúsculas, sin variantes).
- Las 27 filas deben quedar completas; el script `calcular_acuerdo.py`
  rechaza cualquier `codigo` vacío.

## 7. Advertencia metodológica

Este libro debe leerse y aplicarse **antes** de ver la hoja de la otra persona
codificadora, y no debe consultarse con ella durante el proceso. El coeficiente
de acuerdo resultante pierde validez si ambas personas coordinan sus
decisiones antes de codificar.
