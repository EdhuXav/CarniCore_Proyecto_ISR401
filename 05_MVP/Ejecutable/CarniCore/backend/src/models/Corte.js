const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const Corte = sequelize.define("Corte", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  tipo_corte: {
    type: DataTypes.ENUM("brazo", "pierna", "costilla", "lomo", "cabeza", "otro"),
    allowNull: false,
  },
  peso_corte: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  fecha_despiece: { type: DataTypes.DATEONLY, allowNull: false, defaultValue: DataTypes.NOW },
}, { tableName: "cortes" });

module.exports = Corte;
