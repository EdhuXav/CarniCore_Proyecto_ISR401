const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const Animal = sequelize.define("Animal", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  numero_arete: { type: DataTypes.STRING(30), unique: true },
  especie: { type: DataTypes.ENUM("res", "cerdo"), allowNull: false },
  peso_vivo: { type: DataTypes.DECIMAL(10, 2) },
  granja_origen: { type: DataTypes.STRING(120) },
}, { tableName: "animales" });

module.exports = Animal;
