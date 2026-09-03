const createCrudController = require("./crudFactory");
const { Animal, Lote } = require("../models");
const base = createCrudController(Animal, { include: [Lote] });

// RF-03: arete único por animal (cerdo/res)
base.create = async (req, res) => {
  try {
    const { numero_arete, especie } = req.body;
    if ((especie === "res" || especie === "cerdo") && !numero_arete) {
      return res.status(400).json({ error: "Para cerdo y res se exige un número de arete único." });
    }
    if (numero_arete) {
      const existente = await Animal.findOne({ where: { numero_arete } });
      if (existente) {
        return res.status(409).json({ error: `El número de arete ${numero_arete} ya existe (duplicidad).` });
      }
    }
    const item = await Animal.create(req.body);
    res.status(201).json(item);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = base;
