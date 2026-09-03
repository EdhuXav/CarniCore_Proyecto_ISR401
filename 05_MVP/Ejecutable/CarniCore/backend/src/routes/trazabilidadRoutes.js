const router = require("express").Router();
const { consultar } = require("../controllers/trazabilidadController");

router.get("/:codigo", consultar); // RF-11

module.exports = router;
