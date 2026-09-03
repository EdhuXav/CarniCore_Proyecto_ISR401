const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const Lote = sequelize.define("Lote", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  codigo_lote: { type: DataTypes.STRING(30), allowNull: false, unique: true },
  fecha_ingreso: { type: DataTypes.DATEONLY, allowNull: false },
  tipo_producto: {
    type: DataTypes.ENUM("res", "cerdo", "pollo"),
    allowNull: false,
  },
  peso_total: { type: DataTypes.DECIMAL(10, 2) },
  estado: {
    type: DataTypes.ENUM("disponible", "pesado", "despostado", "cerrado"),
    defaultValue: "disponible",
  },
}, { tableName: "lotes" });

module.exports = Lote;
