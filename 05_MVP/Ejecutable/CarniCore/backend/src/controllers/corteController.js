const createCrudController = require("./crudFactory");
const { Corte, RegistroPesaje } = require("../models");
const base = createCrudController(Corte, { include: [RegistroPesaje] });

// RF-06: la suma de cortes no debe superar el peso del animal (margen de merma 5%)
base.create = async (req, res) => {
  try {
    const { registro_pesaje_id, peso_corte } = req.body;
    if (registro_pesaje_id) {
      const registro = await RegistroPesaje.findByPk(registro_pesaje_id, { include: [Corte] });
      if (registro) {
        const MARGEN_MERMA = 0.05;
        const pesoMaximo = parseFloat(registro.peso_libras) * (1 + MARGEN_MERMA);
        const sumaActual = (registro.Cortes || []).reduce((acc, c) => acc + parseFloat(c.peso_corte), 0);
        if (sumaActual + parseFloat(peso_corte) > pesoMaximo) {
          return res.status(400).json({
            error: `La suma de los cortes (${(sumaActual + parseFloat(peso_corte)).toFixed(2)} lb) supera el peso del animal permitido (${pesoMaximo.toFixed(2)} lb con merma).`,
          });
        }
      }
    }
    const item = await Corte.create(req.body);
    res.status(201).json(item);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = base;
