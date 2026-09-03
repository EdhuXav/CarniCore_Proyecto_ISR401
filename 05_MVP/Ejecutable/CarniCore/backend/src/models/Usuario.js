const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

/**
 * Usuario del sistema.
 *
 * CORRECCION DE SEGURIDAD (auditoria del 2026-09-03)
 * --------------------------------------------------
 * usuarioController hereda getAll/getById de crudFactory, que hace
 * Model.findAll() sin proyeccion. Como este modelo no excluia password_hash,
 * `GET /api/usuarios` devolvia el hash bcrypt de TODOS los usuarios a
 * cualquier usuario autenticado, incluido el rol carnicero.
 *
 * La intencion de ocultarlo ya estaba en el codigo --create() lo omitia de su
 * respuesta-- pero solo se habia aplicado en uno de los cinco metodos. Se
 * resuelve en el modelo, que es donde no se puede olvidar: defaultScope
 * excluye password_hash en TODA consulta.
 *
 * El login necesita el hash, y para eso existe el scope "conAutenticacion":
 *   Usuario.scope("conAutenticacion").findOne({ where: { correo } })
 */
const Usuario = sequelize.define(
  "Usuario",
  {
    id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
    cedula: {
      type: DataTypes.STRING(13),
      allowNull: false,
      unique: true,
      validate: { len: [10, 13], is: /^[0-9]+$/ },
    },
    nombre: { type: DataTypes.STRING(120), allowNull: false },
    correo: {
      type: DataTypes.STRING(120),
      allowNull: false,
      unique: true,
      validate: { isEmail: true },
    },
    password_hash: { type: DataTypes.STRING(200), allowNull: false },
    rol: {
      type: DataTypes.ENUM(
        "propietaria",
        "administrador_general",
        "encargado_bodega",
        "carnicero"
      ),
      allowNull: false,
    },
    sucursal: { type: DataTypes.STRING(100), defaultValue: "Matriz" },
    activo: { type: DataTypes.BOOLEAN, defaultValue: true },
  },
  {
    tableName: "usuarios",

    // Ninguna consulta devuelve el hash, salvo que se pida el scope explicito.
    defaultScope: {
      attributes: { exclude: ["password_hash"] },
    },
    scopes: {
      // Uso exclusivo de authController.login.
      conAutenticacion: {
        attributes: { include: ["password_hash"] },
      },
    },
  }
);

// Cinturon y tirantes: aunque alguien construya una consulta que salte el
// defaultScope, el hash no se serializa al responder en JSON.
Usuario.prototype.toJSON = function toJSON() {
  const valores = { ...this.get() };
  delete valores.password_hash;
  return valores;
};

module.exports = Usuario;
