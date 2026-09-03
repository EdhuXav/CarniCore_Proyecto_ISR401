const jwt = require("jsonwebtoken");

/**
 * CORRECCION DE SEGURIDAD (auditoria del 2026-09-03)
 * --------------------------------------------------
 * La version anterior era:
 *
 *     const JWT_SECRET = process.env.JWT_SECRET || "carnicore_dev_secret";
 *
 * Ese valor de reserva estaba escrito en el codigo fuente de un repositorio
 * publico. Cualquiera que lo leyera podia firmar un token valido con el rol
 * que quisiera. Y como el Dockerfile fija NODE_ENV=production pero el
 * fallback no distinguia entorno, el despliegue "de produccion" arrancaba con
 * el secreto conocido si la variable faltaba.
 *
 * Ahora el proceso NO ARRANCA sin JWT_SECRET. Fallar al arrancar es preferible
 * a arrancar de forma insegura y en silencio.
 */
const JWT_SECRET = process.env.JWT_SECRET;
const JWT_EXPIRES_IN = process.env.JWT_EXPIRES_IN || "8h";

if (!JWT_SECRET) {
  console.error(
    "\nERROR DE CONFIGURACIÓN: la variable JWT_SECRET no está definida.\n" +
      "  1. cp backend/.env.example backend/.env\n" +
      "  2. Genere un secreto propio:  openssl rand -hex 32\n" +
      "  3. Póngalo en JWT_SECRET dentro de backend/.env\n"
  );
  process.exit(1);
}

if (JWT_SECRET.length < 32) {
  console.warn(
    "AVISO: JWT_SECRET tiene menos de 32 caracteres. Use `openssl rand -hex 32`."
  );
}

// RNF-03: acceso protegido mediante autenticación (usuario/contraseña -> token)
function requireAuth(req, res, next) {
  const header = req.headers.authorization;
  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: "Token de autenticación requerido." });
  }
  const token = header.slice(7).trim();
  try {
    req.user = jwt.verify(token, JWT_SECRET);
    return next();
  } catch (err) {
    return res.status(401).json({ error: "Token inválido o expirado." });
  }
}

module.exports = { requireAuth, JWT_SECRET, JWT_EXPIRES_IN };
