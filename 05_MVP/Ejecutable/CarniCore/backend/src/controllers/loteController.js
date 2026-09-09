const createCrudController = require("./crudFactory");
const { Lote, GuiaOrigen, Animal, RegistroPesaje } = require("../models");
const base = createCrudController(Lote, { include: [GuiaOrigen, Animal] });

// RF-03: un lote no puede registrarse sin guía de origen asociada
base.create = async (req, res) => {
  try {
    const { guia_origen_id } = req.body;
    if (!guia_origen_id) {
      return res.status(400).json({ error: "No se puede registrar un lote sin una guía de origen asociada (RF-02)." });
    }
    const guia = await GuiaOrigen.findByPk(guia_origen_id);
    if (!guia) {
      return res.status(400).json({ error: "La guía de origen indicada no existe." });
    }
    const item = await Lote.create(req.body);
    res.status(201).json(item);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = base;
