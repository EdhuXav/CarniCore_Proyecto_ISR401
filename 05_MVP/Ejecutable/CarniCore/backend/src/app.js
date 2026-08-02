const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const routes = require("./routes");

const app = express();

app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

app.get("/", (req, res) => {
  res.json({
    sistema: "CarniCore API",
    descripcion: "Backend REST para trazabilidad, pesaje inteligente e inventario cárnico.",
    estado: "operativo",
    documentacion: "Ver README.md del proyecto para la lista completa de endpoints.",
  });
});

app.get("/health", (req, res) => res.json({ status: "ok" }));

app.use("/api", routes);

// Manejo de rutas no encontradas
app.use((req, res) => {
  res.status(404).json({ error: "Ruta no encontrada." });
});

// Manejador de errores genérico
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ error: "Error interno del servidor." });
});

module.exports = app;
