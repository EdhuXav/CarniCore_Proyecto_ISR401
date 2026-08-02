const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const CamaraFrigorifica = sequelize.define("CamaraFrigorifica", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  codigo_camara: { type: DataTypes.STRING(20), allowNull: false, unique: true },
  temperatura: { type: DataTypes.DECIMAL(4, 1) },
  capacidad: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  seccion: {
    type: DataTypes.ENUM("res", "cerdo", "pollo", "embutidos"),
    allowNull: false,
  },
}, { tableName: "camaras_frigorificas" });

module.exports = CamaraFrigorifica;
