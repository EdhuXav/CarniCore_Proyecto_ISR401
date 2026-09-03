const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const GuiaOrigen = sequelize.define("GuiaOrigen", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  numero_guia: { type: DataTypes.STRING(40), allowNull: false, unique: true },
  fecha_emision: { type: DataTypes.DATEONLY, allowNull: false },
  cantidad_animales: { type: DataTypes.INTEGER, allowNull: false },
  medico_veterinario: { type: DataTypes.STRING(120) },
  sello_validado: { type: DataTypes.BOOLEAN, defaultValue: false },
}, { tableName: "guias_origen" });

module.exports = GuiaOrigen;
