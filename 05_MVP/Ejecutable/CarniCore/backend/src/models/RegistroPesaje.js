const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const RegistroPesaje = sequelize.define("RegistroPesaje", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  fecha_hora: { type: DataTypes.DATE, allowNull: false, defaultValue: DataTypes.NOW },
  peso_libras: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  precio_libra: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  costo_total: {
    type: DataTypes.VIRTUAL,
    get() {
      const peso = parseFloat(this.getDataValue("peso_libras")) || 0;
      const precio = parseFloat(this.getDataValue("precio_libra")) || 0;
      return +(peso * precio).toFixed(2);
    },
  },
}, { tableName: "registros_pesaje" });

module.exports = RegistroPesaje;
