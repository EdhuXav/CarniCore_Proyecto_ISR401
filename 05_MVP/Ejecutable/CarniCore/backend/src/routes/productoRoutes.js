const router = require("express").Router();
const c = require("../controllers/productoController");

router.get("/vida-util", c.vidaUtil); // RF-08
router.get("/", c.getAll);
router.get("/:id", c.getById);
router.post("/", c.create);
router.put("/:id", c.update);
router.delete("/:id", c.remove);

module.exports = router;
