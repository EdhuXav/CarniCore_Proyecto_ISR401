const bcrypt = require("bcryptjs");
const createCrudController = require("./crudFactory");
const { Usuario } = require("../models");

const base = createCrudController(Usuario);

/**
 * Cambios respecto de la version anterior (auditoria del 2026-09-03):
 *
 *  - update() pasaba req.body ENTERO a item.update(). Un usuario autenticado
 *    con cualquier rol podia enviar {"rol":"propietaria"} sobre su propio
 *    registro y escalar privilegios, o sobrescribir password_hash con un
 *    valor conocido. Ahora hay lista blanca de campos y el cambio de rol esta
 *    restringido.
 *  - password_hash ya no se expone: lo garantiza el defaultScope del modelo,
 *    y ademas Usuario.prototype.toJSON lo elimina de la serializacion.
 *  - La contrasena minima sube de 6 a 10 caracteres. Seis caracteres no
 *    protegen nada.
 *
 * El control de acceso por rol se aplica en routes/usuarioRoutes.js, con el
 * middleware requireRol.
 */

const CAMPOS_EDITABLES = ["nombre", "correo", "sucursal", "cedula"];
const ROLES_QUE_ASIGNAN_ROL = ["propietaria", "administrador_general"];
const LONGITUD_MINIMA_PASSWORD = 10;

base.create = async (req, res) => {
  try {
    const { password, ...resto } = req.body || {};

    if (!password || password.length < LONGITUD_MINIMA_PASSWORD) {
      return res.status(400).json({
        error: `La contraseña debe tener al menos ${LONGITUD_MINIMA_PASSWORD} caracteres.`,
      });
    }

    // Nunca se acepta un hash suministrado por el cliente.
    delete resto.password_hash;

    const password_hash = await bcrypt.hash(password, 12);
    const item = await Usuario.create({ ...resto, password_hash });

    // toJSON del modelo ya elimina el hash.
    return res.status(201).json(item.toJSON());
  } catch (err) {
    return res.status(400).json({ error: err.message });
  }
};

base.update = async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    if (!usuario) return res.status(404).json({ error: "Usuario no encontrado" });

    // Lista blanca: solo se actualiza lo que esta explicitamente permitido.
    const cambios = {};
    for (const campo of CAMPOS_EDITABLES) {
      if (Object.prototype.hasOwnProperty.call(req.body || {}, campo)) {
        cambios[campo] = req.body[campo];
      }
    }

    // El rol solo lo cambia quien tiene potestad, y nunca sobre si mismo.
    if (req.body && req.body.rol !== undefined) {
      if (!ROLES_QUE_ASIGNAN_ROL.includes(req.user.rol)) {
        return res.status(403).json({
          error: "No tiene permisos para modificar el rol de un usuario.",
        });
      }
      if (String(req.user.id) === String(usuario.id)) {
        return res.status(403).json({
          error: "No puede modificar su propio rol.",
        });
      }
      cambios.rol = req.body.rol;
    }

    // El cambio de contrasena tiene su propia ruta y su propia validacion.
    if (req.body && (req.body.password || req.body.password_hash)) {
      return res.status(400).json({
        error: "Use PATCH /api/usuarios/:id/password para cambiar la contraseña.",
      });
    }

    await usuario.update(cambios);
    return res.json(usuario.toJSON());
  } catch (err) {
    return res.status(400).json({ error: err.message });
  }
};

base.cambiarPassword = async (req, res) => {
  try {
    const { password } = req.body || {};
    if (!password || password.length < LONGITUD_MINIMA_PASSWORD) {
      return res.status(400).json({
        error: `La contraseña debe tener al menos ${LONGITUD_MINIMA_PASSWORD} caracteres.`,
      });
    }
    const usuario = await Usuario.findByPk(req.params.id);
    if (!usuario) return res.status(404).json({ error: "Usuario no encontrado" });

    // Cada persona cambia la suya; propietaria y administrador, la de otros.
    const esPropia = String(req.user.id) === String(usuario.id);
    if (!esPropia && !ROLES_QUE_ASIGNAN_ROL.includes(req.user.rol)) {
      return res.status(403).json({
        error: "Solo puede cambiar su propia contraseña.",
      });
    }

    usuario.password_hash = await bcrypt.hash(password, 12);
    await usuario.save();
    return res.json({ message: "Contraseña actualizada", id: usuario.id });
  } catch (err) {
    return res.status(400).json({ error: err.message });
  }
};

// RF-15: un usuario desactivado no puede iniciar sesion.
base.desactivar = async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    if (!usuario) return res.status(404).json({ error: "Usuario no encontrado" });
    if (String(req.user.id) === String(usuario.id)) {
      return res.status(403).json({ error: "No puede desactivarse a sí mismo." });
    }
    usuario.activo = false;
    await usuario.save();
    return res.json({ message: "Usuario desactivado", id: usuario.id });
  } catch (err) {
    return res.status(400).json({ error: err.message });
  }
};

base.activar = async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    if (!usuario) return res.status(404).json({ error: "Usuario no encontrado" });
    usuario.activo = true;
    await usuario.save();
    return res.json({ message: "Usuario activado", id: usuario.id });
  } catch (err) {
    return res.status(400).json({ error: err.message });
  }
};

module.exports = base;
