const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const Usuario = sequelize.define("Usuario", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  cedula: { type: DataTypes.STRING(13), allowNull: false, unique: true },
  nombre: { type: DataTypes.STRING(120), allowNull: false },
  correo: { type: DataTypes.STRING(120), allowNull: false, unique: true },
  password_hash: { type: DataTypes.STRING(200), allowNull: false },
  rol: {
    type: DataTypes.ENUM("propietaria", "administrador_general", "encargado_bodega", "carnicero"),
    allowNull: false,
  },
  sucursal: { type: DataTypes.STRING(100), defaultValue: "Matriz" },
  activo: { type: DataTypes.BOOLEAN, defaultValue: true },
}, { tableName: "usuarios" });

module.exports = Usuario;
