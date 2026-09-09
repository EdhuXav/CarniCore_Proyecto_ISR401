const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const BajaProducto = sequelize.define("BajaProducto", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  motivo: {
    type: DataTypes.ENUM("vencimiento", "deterioro", "corte_energia", "otro"),
    allowNull: false,
  },
  peso_dado_de_baja: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  evidencia_foto_url: { type: DataTypes.STRING(255) },
  aprobado: { type: DataTypes.BOOLEAN, defaultValue: false },
  fecha_aprobacion: { type: DataTypes.DATE },
}, { tableName: "bajas_producto" });

module.exports = BajaProducto;
