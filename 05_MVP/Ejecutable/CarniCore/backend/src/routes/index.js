const router = require("express").Router();

const { requireAuth } = require("../middlewares/auth");

router.use("/auth", require("./authRoutes"));
router.use("/proveedores", requireAuth, require("./proveedorRoutes"));
router.use("/guias-origen", requireAuth, require("./guiaOrigenRoutes"));
router.use("/lotes", requireAuth, require("./loteRoutes"));
router.use("/animales", requireAuth, require("./animalRoutes"));
router.use("/pesajes", requireAuth, require("./pesajeRoutes"));
router.use("/cortes", requireAuth, require("./corteRoutes"));
router.use("/camaras", requireAuth, require("./camaraRoutes"));
router.use("/productos", requireAuth, require("./productoRoutes"));
router.use("/bajas", requireAuth, require("./bajaRoutes"));
router.use("/ventas", requireAuth, require("./ventaRoutes"));
router.use("/movimientos", requireAuth, require("./movimientoRoutes"));
router.use("/usuarios", requireAuth, require("./usuarioRoutes"));
router.use("/trazabilidad", requireAuth, require("./trazabilidadRoutes"));

module.exports = router;
