const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const { Usuario } = require("../models");
const { JWT_SECRET } = require("../middlewares/auth");

async function login(req, res) {
  try {
    const { correo, password } = req.body;
    const usuario = await Usuario.findOne({ where: { correo } });

    if (!usuario) return res.status(401).json({ error: "Credenciales inválidas." });
    if (!usuario.activo) return res.status(403).json({ error: "Usuario desactivado. Contacte al administrador." });

    const valido = await bcrypt.compare(password, usuario.password_hash);
    if (!valido) return res.status(401).json({ error: "Credenciales inválidas." });

    const token = jwt.sign(
      { id: usuario.id, rol: usuario.rol, nombre: usuario.nombre },
      JWT_SECRET,
      { expiresIn: "8h" }
    );

    res.json({
      token,
      usuario: { id: usuario.id, nombre: usuario.nombre, rol: usuario.rol, correo: usuario.correo },
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}

module.exports = { login };
