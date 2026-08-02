const jwt = require("jsonwebtoken");

const JWT_SECRET = process.env.JWT_SECRET || "carnicore_dev_secret";

// RNF-03: acceso protegido mediante autenticación (usuario/contraseña -> token)
function requireAuth(req, res, next) {
  const header = req.headers.authorization;
  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: "Token de autenticación requerido." });
  }
  const token = header.split(" ")[1];
  try {
    const payload = jwt.verify(token, JWT_SECRET);
    req.user = payload;
    next();
  } catch (err) {
    return res.status(401).json({ error: "Token inválido o expirado." });
  }
}

module.exports = { requireAuth, JWT_SECRET };
