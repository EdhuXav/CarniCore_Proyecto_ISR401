const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const ProductoAlmacenado = sequelize.define("ProductoAlmacenado", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  codigo_producto: { type: DataTypes.STRING(20), allowNull: false, unique: true },
  nombre_producto: { type: DataTypes.STRING(120), allowNull: false },
  fecha_ingreso_camara: { type: DataTypes.DATEONLY, allowNull: false, defaultValue: DataTypes.NOW },
  peso_libras: { type: DataTypes.DECIMAL(10, 2), allowNull: false },
  dias_vida_util: { type: DataTypes.INTEGER, allowNull: false, defaultValue: 5 },
  estado: {
    type: DataTypes.ENUM("optimo", "proximo_a_vencer", "vencido", "de_baja", "vendido"),
    defaultValue: "optimo",
  },
}, { tableName: "productos_almacenados" });

module.exports = ProductoAlmacenado;
