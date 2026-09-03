const createCrudController = require("./crudFactory");
const { RegistroPesaje, Animal, Lote } = require("../models");
const base = createCrudController(RegistroPesaje, { include: [Animal, Lote] });

// RF-04: cálculo automático de costo total; rechaza peso <= 0
base.create = async (req, res) => {
  try {
    const { peso_libras, precio_libra } = req.body;
    if (!peso_libras || parseFloat(peso_libras) <= 0) {
      return res.status(400).json({ error: "El peso ingresado debe ser mayor a 0." });
    }
    const item = await RegistroPesaje.create(req.body);
    res.status(201).json({
      ...item.toJSON(),
      costo_total: item.costo_total,
    });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = base;
