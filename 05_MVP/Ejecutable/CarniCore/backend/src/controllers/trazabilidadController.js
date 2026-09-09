const { Animal, Lote, GuiaOrigen, Proveedor, RegistroPesaje, Corte, ProductoAlmacenado, CamaraFrigorifica, Venta } = require("../models");

// RF-11: consulta de trazabilidad completa a partir del arete o código de lote
async function consultar(req, res) {
  try {
    const { codigo } = req.params;

    const animal = await Animal.findOne({
      where: { numero_arete: codigo },
      include: [
        {
          model: Lote,
          include: [{ model: GuiaOrigen, include: [Proveedor] }],
        },
        {
          model: RegistroPesaje,
          include: [
            {
              model: Corte,
              include: [
                {
                  model: ProductoAlmacenado,
                  include: [CamaraFrigorifica, Venta],
                },
              ],
            },
          ],
        },
      ],
    });

    if (!animal) {
      return res.status(404).json({ error: "Registro no encontrado para el arete/código proporcionado." });
    }

    res.json({
      animal: {
        numero_arete: animal.numero_arete,
        especie: animal.especie,
        peso_vivo: animal.peso_vivo,
        granja_origen: animal.granja_origen,
      },
      lote: animal.Lote,
      guia_origen: animal.Lote ? animal.Lote.GuiaOrigen : null,
      proveedor: animal.Lote && animal.Lote.GuiaOrigen ? animal.Lote.GuiaOrigen.Proveedor : null,
      pesajes: animal.RegistroPesajes,
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}

module.exports = { consultar };
