const createCrudController = require("./crudFactory");
const { ProductoAlmacenado, CamaraFrigorifica, MovimientoInventario } = require("../models");
const base = createCrudController(ProductoAlmacenado, { include: [CamaraFrigorifica] });

// RF-07: todo producto almacenado queda asociado a una cámara válida
base.create = async (req, res) => {
  try {
    const { camara_id } = req.body;
    if (!camara_id) {
      return res.status(400).json({ error: "El producto debe asociarse a una cámara frigorífica válida." });
    }
    const camara = await CamaraFrigorifica.findByPk(camara_id);
    if (!camara) return res.status(400).json({ error: "La cámara indicada no existe." });

    const item = await ProductoAlmacenado.create(req.body);
    await MovimientoInventario.create({
      tipo: "ingreso",
      cantidad_libras: item.peso_libras,
      producto_id: item.id,
      camara_id: camara.id,
      descripcion: `Ingreso de ${item.nombre_producto} a ${camara.codigo_camara}`,
    });
    res.status(201).json(item);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

// RF-08: calcula días restantes de vida útil y clasifica el estado
base.vidaUtil = async (req, res) => {
  try {
    const productos = await ProductoAlmacenado.findAll({ include: [CamaraFrigorifica] });
    const hoy = new Date();

    const resultado = productos.map((p) => {
      const ingreso = new Date(p.fecha_ingreso_camara);
      const diasTranscurridos = Math.floor((hoy - ingreso) / (1000 * 60 * 60 * 24));
      const diasRestantes = p.dias_vida_util - diasTranscurridos;

      let estado = "optimo";
      if (diasRestantes < 0) estado = "vencido";
      else if (diasRestantes <= 1) estado = "proximo_a_vencer";

      return {
        id: p.id,
        producto: p.nombre_producto,
        camara: p.CamaraFrigorifica ? p.CamaraFrigorifica.codigo_camara : null,
        dias_vida_util: p.dias_vida_util,
        dias_restantes: diasRestantes,
        estado,
      };
    });

    res.json(resultado);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

module.exports = base;
