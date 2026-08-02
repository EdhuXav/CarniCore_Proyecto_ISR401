const bcrypt = require("bcryptjs");
const createCrudController = require("./crudFactory");
const { Usuario } = require("../models");
const base = createCrudController(Usuario);

// RNF-03: contraseñas almacenadas con hash + salting (bcrypt)
base.create = async (req, res) => {
  try {
    const { password, ...rest } = req.body;
    if (!password || password.length < 6) {
      return res.status(400).json({ error: "La contraseña debe tener al menos 6 caracteres." });
    }
    const password_hash = await bcrypt.hash(password, 10);
    const item = await Usuario.create({ ...rest, password_hash });
    const { password_hash: _omit, ...safe } = item.toJSON();
    res.status(201).json(safe);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

// RF-15: un usuario desactivado no puede iniciar sesión
base.desactivar = async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    if (!usuario) return res.status(404).json({ error: "Usuario no encontrado" });
    usuario.activo = false;
    await usuario.save();
    res.json({ message: "Usuario desactivado", id: usuario.id });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

base.activar = async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    if (!usuario) return res.status(404).json({ error: "Usuario no encontrado" });
    usuario.activo = true;
    await usuario.save();
    res.json({ message: "Usuario activado", id: usuario.id });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = base;
