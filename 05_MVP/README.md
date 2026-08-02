# CarniCore — Sistema de Trazabilidad, Pesaje Inteligente e Inventario

Proyecto compuesto por dos partes:

```
CarniCore/
├── frontend/          → Interfaz visual (HTML + CSS + JS, sin lógica de negocio)
├── backend/            → API REST (Node.js + Express + Sequelize)
├── docker-compose.yml  → Orquesta PostgreSQL + backend en Docker
└── README.md           → Este archivo
```

El **frontend** es el prototipo visual que ya conoces (login, dashboard y los 21 módulos).
El **backend** es una API REST real, conectada a una base de datos **PostgreSQL**, que implementa
los requisitos funcionales del ERS (RF-01 a RF-16): proveedores, guías de origen, lotes/animales,
pesaje inteligente, despiece, cámaras frigoríficas, inventario, vida útil, bajas, ventas,
movimientos, trazabilidad y usuarios/roles.

---

## 1. Requisitos previos

Solo necesitas tener instalado:

- **Docker Desktop** (incluye Docker Engine y Docker Compose)
  - Windows / Mac: https://www.docker.com/products/docker-desktop/
  - Linux: `sudo apt install docker.io docker-compose-plugin` (o el gestor de tu distro)
- Verifica que quedó instalado abriendo una terminal y ejecutando:

```bash
docker --version
docker compose version
```

Si ambos comandos muestran una versión, estás listo. No necesitas instalar Node.js ni
PostgreSQL en tu computadora: todo corre dentro de contenedores.

---

## 2. Levantar el backend + base de datos con Docker

### Paso 1 — Ubícate en la carpeta del proyecto

Abre una terminal (CMD, PowerShell, Terminal de Mac/Linux) y navega hasta la carpeta
`CarniCore/` (la que contiene el archivo `docker-compose.yml`):

```bash
cd ruta/donde/descomprimiste/CarniCore
```

### Paso 2 — Revisa el archivo de variables de entorno (opcional)

El backend ya trae un archivo `backend/.env` con valores por defecto que funcionan de
inmediato. Si quieres cambiar el usuario, contraseña o el secreto de sesión, edita:

```
backend/.env
```

Si prefieres partir de cero, puedes copiar el ejemplo:

```bash
cp backend/.env.example backend/.env
```

### Paso 3 — Construye y levanta los contenedores

```bash
docker compose up -d --build
```

Esto hace lo siguiente automáticamente:

1. Descarga la imagen de **PostgreSQL 16** y crea la base de datos `carnicore`.
2. Construye la imagen del **backend** (Node.js 18) e instala sus dependencias.
3. Levanta ambos contenedores en segundo plano (`-d`).
4. El backend espera a que PostgreSQL esté "healthy" antes de iniciar.
5. Al arrancar, el backend crea automáticamente todas las tablas (Sequelize `sync`).

### Paso 4 — Verifica que todo esté corriendo

```bash
docker compose ps
```

Deberías ver dos servicios en estado `running`/`healthy`: `carnicore_postgres` y
`carnicore_backend`.

Revisa los logs del backend para confirmar la conexión exitosa:

```bash
docker compose logs -f backend
```

Busca las líneas:

```
✅ Conexión a PostgreSQL establecida correctamente.
✅ Modelos sincronizados con la base de datos.
🥩 CarniCore API escuchando en http://localhost:4000
```

Presiona `Ctrl + C` para salir de los logs (los contenedores siguen corriendo).

### Paso 5 — Prueba la API

Abre tu navegador en:

```
http://localhost:4000
```

Deberías ver un JSON de bienvenida. También puedes probar el endpoint de salud:

```
http://localhost:4000/health
```

### Paso 6 — Carga los datos de ejemplo (seed)

El backend arranca con las tablas vacías. Para poblarlo con proveedores, guías, lotes,
pesajes, cámaras, inventario, usuarios de prueba, etc. (los mismos datos que ves en el
prototipo visual), ejecuta:

```bash
docker compose exec backend npm run seed
```

Al finalizar verás en consola los usuarios de prueba creados, por ejemplo:

```
Usuarios de prueba (contraseña para todos: carnicore2026):
 - gisela.ibanez@carnicore.ec   (propietaria)
 - juan.ramirez@carnicore.ec    (administrador_general)
 - maria.paredes@carnicore.ec   (encargado_bodega)
 - carlos.toapanta@carnicore.ec (carnicero, inactivo)
```

> ⚠️ El seed borra y vuelve a crear todas las tablas (`sync({ force: true })`), así que
> solo debes correrlo la primera vez o cuando quieras reiniciar los datos de prueba.

### Paso 7 — Inicia sesión y prueba un endpoint protegido

```bash
curl -X POST http://localhost:4000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"correo":"gisela.ibanez@carnicore.ec","password":"carnicore2026"}'
```

La respuesta incluye un `token` JWT. Úsalo para consultar cualquier endpoint protegido:

```bash
curl http://localhost:4000/api/proveedores \
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

---

## 3. Abrir el frontend

El frontend sigue siendo estático (no necesita Node ni Docker). Simplemente abre
`frontend/login.html` con doble clic, o sírvelo con cualquier servidor local, por ejemplo:

```bash
cd frontend
python3 -m http.server 8080
```

y visita `http://localhost:8080`.

> El frontend entregado es un **prototipo visual** (botones que solo navegan entre
> páginas). Conectarlo al backend real (fetch a `http://localhost:4000/api/...`) es un
> paso de integración adicional que no está incluido en esta entrega, pero la API ya
> está lista para consumirse.

---

## 4. Comandos útiles del día a día

| Acción | Comando |
|---|---|
| Levantar todo | `docker compose up -d --build` |
| Ver estado de los contenedores | `docker compose ps` |
| Ver logs del backend en vivo | `docker compose logs -f backend` |
| Ver logs de PostgreSQL | `docker compose logs -f postgres` |
| Detener los contenedores | `docker compose down` |
| Detener y borrar también los datos de la BD | `docker compose down -v` |
| Reconstruir el backend tras cambiar código | `docker compose up -d --build backend` |
| Ejecutar el seed manualmente | `docker compose exec backend npm run seed` |
| Entrar a la consola de PostgreSQL | `docker compose exec postgres psql -U carnicore_user -d carnicore` |
| Abrir una terminal dentro del backend | `docker compose exec backend sh` |

---

## 5. (Opcional) Explorar la base de datos con pgAdmin

El `docker-compose.yml` incluye un servicio opcional de **pgAdmin** para explorar las
tablas desde el navegador, desactivado por defecto. Para activarlo:

```bash
docker compose --profile tools up -d pgadmin
```

Luego abre `http://localhost:5050` e inicia sesión con:

- **Correo:** `admin@carnicore.ec`
- **Contraseña:** `carnicore_pass`

Al agregar un nuevo servidor dentro de pgAdmin, usa como *Host* el nombre del contenedor:
`postgres`, puerto `5432`, base de datos `carnicore`, usuario `carnicore_user`,
contraseña `carnicore_pass`.

---

## 6. Estructura del backend

```
backend/
├── Dockerfile
├── package.json
├── .env / .env.example
└── src/
    ├── app.js              → Configuración de Express (middlewares, rutas, errores)
    ├── server.js           → Arranque del servidor + conexión a PostgreSQL con reintentos
    ├── config/db.js        → Configuración de conexión Sequelize
    ├── models/             → Un archivo por entidad + index.js con las asociaciones
    ├── controllers/        → Lógica de cada módulo (incluye validaciones del ERS)
    ├── routes/              → Definición de endpoints REST por módulo
    ├── middlewares/auth.js  → Protección de rutas mediante JWT
    └── seed/seed.js         → Script para poblar datos de ejemplo
```

### Endpoints principales

| Módulo | Base URL | Requisito ERS |
|---|---|---|
| Autenticación | `POST /api/auth/login` | RNF-03 |
| Proveedores | `/api/proveedores` | RF-01 |
| Guías de origen | `/api/guias-origen` | RF-02 |
| Lotes | `/api/lotes` | RF-03 |
| Animales | `/api/animales` | RF-03 |
| Pesajes | `/api/pesajes` | RF-04 / RF-05 |
| Cortes (despiece) | `/api/cortes` | RF-06 |
| Cámaras frigoríficas | `/api/camaras` | RF-07 |
| Productos / inventario | `/api/productos` | RF-07 |
| Vida útil | `GET /api/productos/vida-util` | RF-08 |
| Bajas de producto | `/api/bajas` (+ `PATCH /:id/aprobar`) | RF-09 |
| Ventas | `/api/ventas` | RF-10 |
| Trazabilidad | `GET /api/trazabilidad/:codigo` | RF-11 |
| Movimientos de inventario | `/api/movimientos` | RF-16 |
| Usuarios | `/api/usuarios` (+ `PATCH /:id/activar` / `desactivar`) | RF-15 |

Todos los endpoints (excepto `/api/auth/login`) requieren el header
`Authorization: Bearer <token>` obtenido al iniciar sesión.

---

## 7. Solución de problemas

**"port is already allocated" al levantar los contenedores**
Otro proceso está usando el puerto 4000 o 5432. Detén ese proceso o cambia el mapeo de
puertos en `docker-compose.yml` (por ejemplo `"4001:4000"`).

**El backend se reinicia en bucle / no conecta a la base de datos**
Revisa los logs con `docker compose logs -f postgres` y `docker compose logs -f backend`.
El backend reintenta la conexión automáticamente durante ~45 segundos antes de fallar.

**Quiero borrar todo y empezar de cero**
```bash
docker compose down -v
docker compose up -d --build
docker compose exec backend npm run seed
```

**Cambié el código del backend y no se refleja**
```bash
docker compose up -d --build backend
```
