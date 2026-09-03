require("dotenv").config();

const app = require("./app");
const { sequelize } = require("./models");

const PORT = process.env.PORT || 4000;
const MAX_REINTENTOS = 15;
const ESPERA_MS = 3000;

/**
 * Cambio respecto de la version anterior (auditoria del 2026-09-03):
 *
 * El arranque hacia `sequelize.sync({ alter: true })` incondicionalmente, y el
 * Dockerfile fija NODE_ENV=production. `alter: true` inspecciona el esquema en
 * vivo y emite ALTER TABLE para cuadrarlo con los modelos: en produccion puede
 * borrar columnas o reescribir tipos sin aviso, sobre datos reales.
 *
 * Ahora `alter` solo actua fuera de produccion. En produccion el esquema se
 * gestiona con migraciones versionadas, que ademas dejan rastro en el
 * repositorio -- justo lo que el paragrafo 5.1 pide de cualquier
 * transformacion de datos.
 */
const enProduccion = process.env.NODE_ENV === "production";

async function conectarConReintentos(reintentos = MAX_REINTENTOS) {
  try {
    await sequelize.authenticate();
    console.log("Conexión a PostgreSQL establecida correctamente.");

    if (enProduccion) {
      console.log(
        "NODE_ENV=production: no se sincroniza el esquema automáticamente. " +
          "Aplique las migraciones antes de desplegar."
      );
    } else {
      await sequelize.sync({ alter: true });
      console.log("Modelos sincronizados con la base de datos (modo desarrollo).");
    }
  } catch (err) {
    if (reintentos === 0) {
      console.error("No fue posible conectar con PostgreSQL:", err.message);
      process.exit(1);
    }
    console.log(
      `PostgreSQL no está listo aún. Reintentando en ${ESPERA_MS / 1000}s... ` +
        `(${reintentos} intentos restantes)`
    );
    await new Promise((resolver) => setTimeout(resolver, ESPERA_MS));
    return conectarConReintentos(reintentos - 1);
  }
}

(async () => {
  await conectarConReintentos();
  const servidor = app.listen(PORT, () => {
    console.log(`CarniCore API escuchando en http://localhost:${PORT}`);
  });

  // Cierre ordenado: sin esto, docker compose down deja peticiones a medias.
  for (const senal of ["SIGTERM", "SIGINT"]) {
    process.on(senal, () => {
      console.log(`\n${senal} recibida. Cerrando de forma ordenada...`);
      servidor.close(async () => {
        await sequelize.close();
        process.exit(0);
      });
    });
  }
})();
