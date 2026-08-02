require("dotenv").config();

const app = require("./app");
const { sequelize } = require("./models");

const PORT = process.env.PORT || 4000;
const MAX_RETRIES = 15;
const RETRY_DELAY_MS = 3000;

async function connectWithRetry(retries = MAX_RETRIES) {
  try {
    await sequelize.authenticate();
    console.log("✅ Conexión a PostgreSQL establecida correctamente.");

    // Sincroniza los modelos con la base de datos (crea tablas si no existen)
    await sequelize.sync({ alter: true });
    console.log("✅ Modelos sincronizados con la base de datos.");
  } catch (err) {
    if (retries === 0) {
      console.error("❌ No fue posible conectar con PostgreSQL:", err.message);
      process.exit(1);
    }
    console.log(`⏳ PostgreSQL no está listo aún. Reintentando en ${RETRY_DELAY_MS / 1000}s... (${retries} intentos restantes)`);
    await new Promise((resolve) => setTimeout(resolve, RETRY_DELAY_MS));
    return connectWithRetry(retries - 1);
  }
}

(async () => {
  await connectWithRetry();
  app.listen(PORT, () => {
    console.log(`🥩 CarniCore API escuchando en http://localhost:${PORT}`);
  });
})();
