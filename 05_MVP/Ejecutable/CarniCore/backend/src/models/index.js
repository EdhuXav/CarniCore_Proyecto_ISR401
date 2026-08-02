const sequelize = require("../config/db");

const Usuario = require("./Usuario");
const Proveedor = require("./Proveedor");
const GuiaOrigen = require("./GuiaOrigen");
const Lote = require("./Lote");
const Animal = require("./Animal");
const RegistroPesaje = require("./RegistroPesaje");
const Corte = require("./Corte");
const CamaraFrigorifica = require("./CamaraFrigorifica");
const ProductoAlmacenado = require("./ProductoAlmacenado");
const BajaProducto = require("./BajaProducto");
const Venta = require("./Venta");
const MovimientoInventario = require("./MovimientoInventario");

/* =========================================================
   Asociaciones — reflejan el diagrama de clases conceptual
   del ERS (Cap. 4.3)
   ========================================================= */

// Proveedor 1—N GuiaOrigen
Proveedor.hasMany(GuiaOrigen, { foreignKey: "proveedor_id" });
GuiaOrigen.belongsTo(Proveedor, { foreignKey: "proveedor_id" });

// GuiaOrigen 1—N Lote
GuiaOrigen.hasMany(Lote, { foreignKey: "guia_origen_id" });
Lote.belongsTo(GuiaOrigen, { foreignKey: "guia_origen_id" });

// Lote 1—N Animal (cerdo/res); para aves el lote no requiere animales individuales
Lote.hasMany(Animal, { foreignKey: "lote_id" });
Animal.belongsTo(Lote, { foreignKey: "lote_id" });

// Animal / Lote 1—N RegistroPesaje
Lote.hasMany(RegistroPesaje, { foreignKey: "lote_id" });
RegistroPesaje.belongsTo(Lote, { foreignKey: "lote_id" });
Animal.hasMany(RegistroPesaje, { foreignKey: "animal_id" });
RegistroPesaje.belongsTo(Animal, { foreignKey: "animal_id" });

// RegistroPesaje 1—N Corte (despiece)
RegistroPesaje.hasMany(Corte, { foreignKey: "registro_pesaje_id" });
Corte.belongsTo(RegistroPesaje, { foreignKey: "registro_pesaje_id" });

// CamaraFrigorifica 1—N ProductoAlmacenado
CamaraFrigorifica.hasMany(ProductoAlmacenado, { foreignKey: "camara_id" });
ProductoAlmacenado.belongsTo(CamaraFrigorifica, { foreignKey: "camara_id" });

// Corte 1—1 ProductoAlmacenado (opcional, el corte puede pasar a cámara)
Corte.hasOne(ProductoAlmacenado, { foreignKey: "corte_id" });
ProductoAlmacenado.belongsTo(Corte, { foreignKey: "corte_id" });

// ProductoAlmacenado 1—N BajaProducto
ProductoAlmacenado.hasMany(BajaProducto, { foreignKey: "producto_id" });
BajaProducto.belongsTo(ProductoAlmacenado, { foreignKey: "producto_id" });

// Usuario 1—N BajaProducto (supervisor que aprueba)
Usuario.hasMany(BajaProducto, { foreignKey: "supervisor_id" });
BajaProducto.belongsTo(Usuario, { foreignKey: "supervisor_id", as: "supervisor" });

// ProductoAlmacenado 1—N Venta
ProductoAlmacenado.hasMany(Venta, { foreignKey: "producto_id" });
Venta.belongsTo(ProductoAlmacenado, { foreignKey: "producto_id" });

// ProductoAlmacenado 1—N MovimientoInventario
ProductoAlmacenado.hasMany(MovimientoInventario, { foreignKey: "producto_id" });
MovimientoInventario.belongsTo(ProductoAlmacenado, { foreignKey: "producto_id" });
CamaraFrigorifica.hasMany(MovimientoInventario, { foreignKey: "camara_id" });
MovimientoInventario.belongsTo(CamaraFrigorifica, { foreignKey: "camara_id" });

module.exports = {
  sequelize,
  Usuario,
  Proveedor,
  GuiaOrigen,
  Lote,
  Animal,
  RegistroPesaje,
  Corte,
  CamaraFrigorifica,
  ProductoAlmacenado,
  BajaProducto,
  Venta,
  MovimientoInventario,
};
