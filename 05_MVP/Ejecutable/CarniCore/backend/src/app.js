const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const morgan = require("morgan");
const rateLimit = require("express-rate-limit");

const routes = require("./routes");

const app = express();

/**
 * Cambios respecto de la version anterior (auditoria del 2026-09-03):
 *
 *  - helmet: cabeceras de seguridad HTTP. No habia ninguna.
 *  - CORS con lista blanca. Antes era app.use(cors()) sin origen: cualquier
 *    sitio web podia llamar a la API desde el navegador de un usuario.
 *  - Limite de peticiones en /api/auth: sin el, la fuerza bruta contra el
 *    login no tiene ningun freno.
 *  - Limite de tamano en el cuerpo JSON.
 *  - El manejador de errores se registra DESPUES del 404. En la version
 *    anterior el 404 era un app.use() sin ruta y capturaba todo antes, de
 *    modo que el manejador de errores de 4 argumentos nunca se alcanzaba.
 */

app.disable("x-powered-by");
app.use(helmet());

const ORIGENES = (process.env.CORS_ORIGIN || "")
  .split(",")
  .map((o) => o.trim())
  .filter(Boolean);

app.use(
  cors({
    origin(origin, callback) {
      // Peticiones sin origen (curl, Postman, healthcheck) se permiten.
      if (!origin) return callback(null, true);
      if (ORIGENES.length === 0 || ORIGENES.includes(origin)) {
        return callback(null, true);
      }
      return callback(new Error("Origen no permitido por la política CORS."));
    },
    credentials: true,
  })
);

app.use(express.json({ limit: "1mb" }));
app.use(morgan(process.env.NODE_ENV === "production" ? "combined" : "dev"));

// Fuerza bruta contra el login: 10 intentos cada 15 minutos por IP.
const limitadorAuth = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "Demasiados intentos. Espere unos minutos e inténtelo de nuevo." },
});

// Limite general, holgado, para el resto de la API.
const limitadorGeneral = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 1000,
  standardHeaders: true,
  legacyHeaders: false,
});

app.get("/", (req, res) => {
  res.json({
    sistema: "CarniCore API",
    descripcion:
      "Backend REST para trazabilidad, pesaje inteligente e inventario cárnico.",
    estado: "operativo",
    documentacion: "Ver README.md del proyecto para la lista completa de endpoints.",
  });
});

app.get("/health", (req, res) => res.json({ status: "ok" }));

app.use("/api/auth", limitadorAuth);
app.use("/api", limitadorGeneral, routes);

// 404: cualquier ruta no reconocida.
app.use((req, res) => {
  res.status(404).json({ error: "Ruta no encontrada." });
});

// Manejador de errores. Va el ultimo, y con cuatro argumentos, o Express no
// lo reconoce como manejador de errores.
// eslint-disable-next-line no-unused-vars
app.use((err, req, res, next) => {
  console.error(err);
  const estado = err.status || 500;
  res.status(estado).json({
    error:
      estado === 500
        ? "Error interno del servidor."
        : err.message || "Solicitud incorrecta.",
  });
});

module.exports = app;
