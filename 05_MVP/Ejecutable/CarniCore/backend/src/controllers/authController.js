const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const { Usuario } = require("../models");
const { JWT_SECRET, JWT_EXPIRES_IN } = require("../middlewares/auth");

/**
 * Cambios respecto de la version anterior (auditoria del 2026-09-03):
 *
 *  - Usa el scope "conAutenticacion" para traer el hash. El defaultScope del
 *    modelo lo excluye ahora en todas las demas consultas.
 *  - El bloque catch ya no devuelve err.message al cliente: filtraba detalles
 *    internos (nombres de tabla, errores de conexion) en una ruta publica y
 *    sin autenticar, que es justo donde no conviene.
 *  - Compara el hash aunque el usuario no exista, para no revelar por tiempo
 *    de respuesta que correos estan dados de alta.
 */

// Hash de descarte, para que el coste de bcrypt sea el mismo exista o no el
// usuario. Evita la enumeracion de correos por diferencia de tiempos.
const HASH_SENUELO = "$2a$10$abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX";

async function login(req, res) {
  try {
    const { correo, password } = req.body || {};

    if (!correo || !password) {
      return res.status(400).json({ error: "Correo y contraseña son obligatorios." });
    }

    const usuario = await Usuario.scope("conAutenticacion").findOne({
      where: { correo },
    });

    const hash = usuario ? usuario.password_hash : HASH_SENUELO;
    const valido = await bcrypt.compare(password, hash);

    // Mismo mensaje en los dos casos: no se revela si el correo existe.
    if (!usuario || !valido) {
      return res.status(401).json({ error: "Credenciales inválidas." });
    }

    if (!usuario.activo) {
      // RF-15: un usuario desactivado no puede iniciar sesion.
      return res.status(403).json({
        error: "Usuario desactivado. Contacte al administrador.",
      });
    }

    const token = jwt.sign(
      { id: usuario.id, rol: usuario.rol, nombre: usuario.nombre },
      JWT_SECRET,
      { expiresIn: JWT_EXPIRES_IN }
    );

    return res.json({
      token,
      usuario: {
        id: usuario.id,
        nombre: usuario.nombre,
        rol: usuario.rol,
        correo: usuario.correo,
      },
    });
  } catch (err) {
    console.error("Error en login:", err);
    return res.status(500).json({ error: "Error interno del servidor." });
  }
}

module.exports = { login };
