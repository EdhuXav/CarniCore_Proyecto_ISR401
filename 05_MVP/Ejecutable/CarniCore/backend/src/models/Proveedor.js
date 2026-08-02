const { DataTypes } = require("sequelize");
const sequelize = require("../config/db");

const Proveedor = sequelize.define("Proveedor", {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  ruc: {
    type: DataTypes.STRING(13),
    allowNull: false,
    unique: true,
    validate: { len: [13, 13] },
  },
  nombre: { type: DataTypes.STRING(150), allowNull: false },
  tipo_animal: {
    type: DataTypes.ENUM("res", "cerdo", "pollo", "mixto"),
    allowNull: false,
  },
  registro_sanitario: { type: DataTypes.STRING(60) },
  estado_sri: {
    type: DataTypes.ENUM("regularizado", "pendiente", "vencido"),
    defaultValue: "pendiente",
  },
}, { tableName: "proveedores" });

module.exports = Proveedor;
