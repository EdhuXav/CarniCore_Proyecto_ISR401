require("dotenv").config();
const bcrypt = require("bcryptjs");

const {
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
} = require("../models");

async function seed() {
  console.log("🌱 Sincronizando base de datos...");
  await sequelize.sync({ force: true });

  console.log("🌱 Creando usuarios...");
  const passwordHash = await bcrypt.hash("carnicore2026", 10);
  const propietaria = await Usuario.create({
    cedula: "1712345678",
    nombre: "Gisela Ibáñez",
    correo: "gisela.ibanez@carnicore.ec",
    password_hash: passwordHash,
    rol: "propietaria",
  });
  const adminGeneral = await Usuario.create({
    cedula: "1798765432",
    nombre: "Juan Ramírez",
    correo: "juan.ramirez@carnicore.ec",
    password_hash: passwordHash,
    rol: "administrador_general",
  });
  await Usuario.create({
    cedula: "1755566677",
    nombre: "María Paredes",
    correo: "maria.paredes@carnicore.ec",
    password_hash: passwordHash,
    rol: "encargado_bodega",
  });
  await Usuario.create({
    cedula: "1733322211",
    nombre: "Carlos Toapanta",
    correo: "carlos.toapanta@carnicore.ec",
    password_hash: passwordHash,
    rol: "carnicero",
    activo: false,
  });

  console.log("🌱 Creando proveedores...");
  const provSanVicente = await Proveedor.create({
    ruc: "1892034561001",
    nombre: "Granja San Vicente",
    tipo_animal: "res",
    registro_sanitario: "AGR-2026-0113",
    estado_sri: "regularizado",
  });
  const provElRoble = await Proveedor.create({
    ruc: "1801122334001",
    nombre: "Porcícola El Roble",
    tipo_animal: "cerdo",
    registro_sanitario: "AGR-2026-0087",
    estado_sri: "regularizado",
  });
  const provLosAndes = await Proveedor.create({
    ruc: "1723456789001",
    nombre: "Avícola Los Andes",
    tipo_animal: "pollo",
    registro_sanitario: "AGR-2026-0221",
    estado_sri: "pendiente",
  });

  console.log("🌱 Creando guías de origen...");
  const guiaSV = await GuiaOrigen.create({
    numero_guia: "AGR-2026-0113",
    fecha_emision: "2026-07-28",
    cantidad_animales: 4,
    medico_veterinario: "Dr. F. Naranjo",
    sello_validado: true,
    proveedor_id: provSanVicente.id,
  });
  const guiaER = await GuiaOrigen.create({
    numero_guia: "AGR-2026-0087",
    fecha_emision: "2026-07-27",
    cantidad_animales: 6,
    medico_veterinario: "Dra. M. Salazar",
    sello_validado: true,
    proveedor_id: provElRoble.id,
  });
  await GuiaOrigen.create({
    numero_guia: "AGR-2026-0221",
    fecha_emision: "2026-07-26",
    cantidad_animales: 120,
    medico_veterinario: null,
    sello_validado: false,
    proveedor_id: provLosAndes.id,
  });

  console.log("🌱 Creando lotes y animales...");
  const loteRes = await Lote.create({
    codigo_lote: "L-RES-0481",
    fecha_ingreso: "2026-08-02",
    tipo_producto: "res",
    peso_total: 312,
    estado: "despostado",
    guia_origen_id: guiaSV.id,
  });
  const loteCerdo = await Lote.create({
    codigo_lote: "L-CER-0502",
    fecha_ingreso: "2026-08-02",
    tipo_producto: "cerdo",
    peso_total: 96,
    estado: "pesado",
    guia_origen_id: guiaER.id,
  });

  const animalRes = await Animal.create({
    numero_arete: "AR-000481",
    especie: "res",
    peso_vivo: 340,
    granja_origen: "Granja San Vicente",
    lote_id: loteRes.id,
  });
  const animalCerdo = await Animal.create({
    numero_arete: "AR-000502",
    especie: "cerdo",
    peso_vivo: 110,
    granja_origen: "Porcícola El Roble",
    lote_id: loteCerdo.id,
  });

  console.log("🌱 Registrando pesajes...");
  const pesajeRes = await RegistroPesaje.create({
    peso_libras: 312,
    precio_libra: 2.1,
    lote_id: loteRes.id,
    animal_id: animalRes.id,
  });
  await RegistroPesaje.create({
    peso_libras: 96,
    precio_libra: 1.85,
    lote_id: loteCerdo.id,
    animal_id: animalCerdo.id,
  });

  console.log("🌱 Registrando cortes de despiece...");
  const corteBrazo = await Corte.create({ tipo_corte: "brazo", peso_corte: 45, registro_pesaje_id: pesajeRes.id });
  const cortePierna = await Corte.create({ tipo_corte: "pierna", peso_corte: 60, registro_pesaje_id: pesajeRes.id });
  const corteCostilla = await Corte.create({ tipo_corte: "costilla", peso_corte: 30, registro_pesaje_id: pesajeRes.id });

  console.log("🌱 Creando cámaras frigoríficas...");
  const camaraRes = await CamaraFrigorifica.create({ codigo_camara: "CAM-RES", temperatura: -1.5, capacidad: 2000, seccion: "res" });
  const camaraCerdo = await CamaraFrigorifica.create({ codigo_camara: "CAM-CER", temperatura: -1.2, capacidad: 1500, seccion: "cerdo" });
  const camaraPollo = await CamaraFrigorifica.create({ codigo_camara: "CAM-POL", temperatura: 2.0, capacidad: 1000, seccion: "pollo" });
  const camaraEmbutidos = await CamaraFrigorifica.create({ codigo_camara: "CAM-EMB", temperatura: 3.5, capacidad: 800, seccion: "embutidos" });

  console.log("🌱 Almacenando productos...");
  const prodBrazo = await ProductoAlmacenado.create({
    codigo_producto: "P-0001", nombre_producto: "Brazo de res", fecha_ingreso_camara: "2026-08-02",
    peso_libras: 45, dias_vida_util: 5, estado: "optimo", camara_id: camaraRes.id, corte_id: corteBrazo.id,
  });
  await ProductoAlmacenado.create({
    codigo_producto: "P-0002", nombre_producto: "Pierna de res", fecha_ingreso_camara: "2026-08-02",
    peso_libras: 60, dias_vida_util: 5, estado: "optimo", camara_id: camaraRes.id, corte_id: cortePierna.id,
  });
  await ProductoAlmacenado.create({
    codigo_producto: "P-0003", nombre_producto: "Costilla de res", fecha_ingreso_camara: "2026-07-29",
    peso_libras: 30, dias_vida_util: 5, estado: "proximo_a_vencer", camara_id: camaraRes.id, corte_id: corteCostilla.id,
  });
  await ProductoAlmacenado.create({
    codigo_producto: "P-0004", nombre_producto: "Chuleta de cerdo", fecha_ingreso_camara: "2026-08-01",
    peso_libras: 52, dias_vida_util: 6, estado: "optimo", camara_id: camaraCerdo.id,
  });
  const prodPollo = await ProductoAlmacenado.create({
    codigo_producto: "P-0005", nombre_producto: "Pollo entero", fecha_ingreso_camara: "2026-07-30",
    peso_libras: 15, dias_vida_util: 3, estado: "vencido", camara_id: camaraPollo.id,
  });
  await ProductoAlmacenado.create({
    codigo_producto: "P-0006", nombre_producto: "Chorizo", fecha_ingreso_camara: "2026-07-28",
    peso_libras: 60, dias_vida_util: 10, estado: "optimo", camara_id: camaraEmbutidos.id,
  });

  console.log("🌱 Registrando una baja de ejemplo...");
  await BajaProducto.create({
    motivo: "vencimiento",
    peso_dado_de_baja: 15,
    evidencia_foto_url: null,
    aprobado: true,
    fecha_aprobacion: new Date(),
    producto_id: prodPollo.id,
    supervisor_id: adminGeneral.id,
  });

  console.log("🌱 Registrando ventas y movimientos...");
  const venta = await Venta.create({
    numero_factura: "001-001-000122",
    cliente: "Mini Market La 9",
    cantidad_libras: 20,
    precio_libra: 2.0,
    producto_id: prodBrazo.id,
  });

  await MovimientoInventario.create({ tipo: "ingreso", cantidad_libras: 312, descripcion: "Ingreso Res, canal #A-1042", camara_id: camaraRes.id });
  await MovimientoInventario.create({ tipo: "venta", cantidad_libras: 20, descripcion: `Venta a ${venta.cliente}`, producto_id: prodBrazo.id, camara_id: camaraRes.id });
  await MovimientoInventario.create({ tipo: "baja", cantidad_libras: 15, descripcion: "Baja por vencimiento - Pollo entero", producto_id: prodPollo.id, camara_id: camaraPollo.id });

  console.log("✅ Datos de ejemplo creados correctamente.");
  console.log("");
  console.log("Usuarios de prueba (contraseña para todos: carnicore2026):");
  console.log(" - gisela.ibanez@carnicore.ec   (propietaria)");
  console.log(" - juan.ramirez@carnicore.ec    (administrador_general)");
  console.log(" - maria.paredes@carnicore.ec   (encargado_bodega)");
  console.log(" - carlos.toapanta@carnicore.ec (carnicero, inactivo)");

  process.exit(0);
}

seed().catch((err) => {
  console.error("❌ Error al poblar la base de datos:", err);
  process.exit(1);
});
