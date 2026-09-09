/**
 * Fábrica de controladores CRUD genéricos.
 * Reduce la repetición para los módulos que solo requieren
 * operaciones estándar de alta, consulta, edición y baja.
 */
function createCrudController(Model, options = {}) {
  const { include = [] } = options;

  return {
    async getAll(req, res) {
      try {
        const items = await Model.findAll({ include, order: [["id", "DESC"]] });
        res.json(items);
      } catch (err) {
        res.status(500).json({ error: err.message });
      }
    },

    async getById(req, res) {
      try {
        const item = await Model.findByPk(req.params.id, { include });
        if (!item) return res.status(404).json({ error: "Registro no encontrado" });
        res.json(item);
      } catch (err) {
        res.status(500).json({ error: err.message });
      }
    },

    async create(req, res) {
      try {
        const item = await Model.create(req.body);
        res.status(201).json(item);
      } catch (err) {
        res.status(400).json({ error: err.message });
      }
    },

    async update(req, res) {
      try {
        const item = await Model.findByPk(req.params.id);
        if (!item) return res.status(404).json({ error: "Registro no encontrado" });
        await item.update(req.body);
        res.json(item);
      } catch (err) {
        res.status(400).json({ error: err.message });
      }
    },

    async remove(req, res) {
      try {
        const item = await Model.findByPk(req.params.id);
        if (!item) return res.status(404).json({ error: "Registro no encontrado" });
        await item.destroy();
        res.status(204).send();
      } catch (err) {
        res.status(500).json({ error: err.message });
      }
    },
  };
}

module.exports = createCrudController;
