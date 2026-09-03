const createCrudController = require("./crudFactory");
const { BajaProducto, ProductoAlmacenado, MovimientoInventario } = require("../models");
const base = createCrudController(BajaProducto, { include: [ProductoAlmacenado] });

// RF-09: la baja no se refleja en el inventario hasta que el admin general la apruebe
base.aprobar = async (req, res) => {
  try {
    const baja = await BajaProducto.findByPk(req.params.id, { include: [ProductoAlmacenado] });
    if (!baja) return res.status(404).json({ error: "Registro de baja no encontrado" });
    if (baja.aprobado) return res.status(400).json({ error: "Esta baja ya fue aprobada." });

    baja.aprobado = true;
    baja.fecha_aprobacion = new Date();
    baja.supervisor_id = req.body.supervisor_id || null;
    await baja.save();

    if (baja.ProductoAlmacenado) {
      baja.ProductoAlmacenado.estado = "de_baja";
      await baja.ProductoAlmacenado.save();

      await MovimientoInventario.create({
        tipo: "baja",
        cantidad_libras: baja.peso_dado_de_baja,
        producto_id: baja.ProductoAlmacenado.id,
        descripcion: `Baja aprobada: ${baja.motivo}`,
      });
    }

    res.json(baja);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = base;
