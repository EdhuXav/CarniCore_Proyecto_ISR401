const router = require("express").Router();
const c = require("../controllers/usuarioController");

router.get("/", c.getAll);
router.get("/:id", c.getById);
router.post("/", c.create);
router.put("/:id", c.update);
router.patch("/:id/desactivar", c.desactivar); // RF-15
router.patch("/:id/activar", c.activar);
router.delete("/:id", c.remove);

module.exports = router;
