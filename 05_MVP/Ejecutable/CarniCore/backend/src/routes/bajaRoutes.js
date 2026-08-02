const router = require("express").Router();
const c = require("../controllers/bajaController");

router.get("/", c.getAll);
router.get("/:id", c.getById);
router.post("/", c.create);
router.put("/:id", c.update);
router.patch("/:id/aprobar", c.aprobar); // RF-09
router.delete("/:id", c.remove);

module.exports = router;
