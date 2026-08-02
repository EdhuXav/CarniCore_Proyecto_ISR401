const createCrudController = require("./crudFactory");
const { Venta, ProductoAlmacenado, MovimientoInventario } = require("../models");
const base = createCrudController(Venta, { include: [ProductoAlmacenado] });

// RF-10: toda venta descuenta el producto del inventario de la cámara de origen
base.create = async (req, res) => {
  try {
    const { producto_id, cantidad_libras } = req.body;
    const producto = await ProductoAlmacenado.findByPk(producto_id);
    if (!producto) return res.status(400).json({ error: "El producto indicado no existe en inventario." });
    if (parseFloat(cantidad_libras) > parseFloat(producto.peso_libras)) {
      return res.status(400).json({ error: "No hay inventario suficiente para completar la venta." });
    }

    const venta = await Venta.create(req.body);

    producto.peso_libras = parseFloat(producto.peso_libras) - parseFloat(cantidad_libras);
    if (producto.peso_libras <= 0) producto.estado = "vendido";
    await producto.save();

    await MovimientoInventario.create({
      tipo: "venta",
      cantidad_libras,
      producto_id: producto.id,
      descripcion: `Venta a ${venta.cliente} · Factura ${venta.numero_factura || "N/D"}`,
    });

    res.status(201).json({ ...venta.toJSON(), total: venta.total });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = base;
