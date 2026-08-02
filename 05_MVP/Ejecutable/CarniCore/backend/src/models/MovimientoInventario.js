const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const MovimientoInventario = sequelize.define("MovimientoInventario", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  tipo: {
    type: DataTypes.ENUM("ingreso", "venta", "baja", "ajuste_conteo"),
    allowNull: false,
  },
  cantidad_libras: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  fecha: { type: DataTypes.DATE, allowNull: false, defaultValue: DataTypes.NOW },
  descripcion: { type: DataTypes.STRING(200) },
}, { tableName: "movimientos_inventario" });

module.exports = MovimientoInventario;
