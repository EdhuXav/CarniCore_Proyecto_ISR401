const createCrudController = require("./crudFactory");
const { Proveedor } = require("../models");
const base = createCrudController(Proveedor);

// Criterio de aceptación RF-01: RUC válido de 13 dígitos
base.create = async (req, res) => {
  try {
    const { ruc } = req.body;
    if (!ruc || !/^\d{13}$/.test(ruc)) {
      return res.status(400).json({ error: "El proveedor requiere un RUC válido de 13 dígitos." });
    }
    const item = await Proveedor.create(req.body);
    res.status(201).json(item);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = base;
