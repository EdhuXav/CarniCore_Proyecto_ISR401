const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const Venta = sequelize.define("Venta", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  numero_factura: { type: DataTypes.STRING(30) },
  cliente: { type: DataTypes.STRING(120), allowNull: false },
  cantidad_libras: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  precio_libra: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  total: {
    type: DataTypes.VIRTUAL,
    get() {
      const c = parseFloat(this.getDataValue("cantidad_libras")) || 0;
      const p = parseFloat(this.getDataValue("precio_libra")) || 0;
      return +(c * p).toFixed(2);
    },
  },
  fecha: { type: DataTypes.DATE, allowNull: false, defaultValue: DataTypes.NOW },
}, { tableName: "ventas" });

module.exports = Venta;
