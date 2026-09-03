const router = require("express").Router();
const c = require("../controllers/bajaController");
const { requireRol, requireNivelMinimo } = require("../middlewares/roles");

/**
 * RF-09: "con aprobacion del administrador general. Una baja no se refleja en
 * el inventario hasta que sea aprobada."
 *
 * La version anterior no comprobaba ningun rol: cualquier usuario autenticado
 * podia aprobar su propia baja, lo que vaciaba de contenido el requisito que
 * la matriz de trazabilidad da por realizado.
 */

const APROBADORES = ["propietaria", "administrador_general"];

router.get("/", requireNivelMinimo("carnicero"), c.getAll);
router.get("/:id", requireNivelMinimo("carnicero"), c.getById);

// Registrar la solicitud de baja puede hacerlo el personal de bodega.
router.post("/", requireNivelMinimo("encargado_bodega"), c.create);

router.put("/:id", requireNivelMinimo("encargado_bodega"), c.update);

// Aprobar es lo que produce el efecto sobre el inventario: solo administracion.
if (typeof c.aprobar === "function") {
  router.patch("/:id/aprobar", requireRol(...APROBADORES), c.aprobar);
}
if (typeof c.rechazar === "function") {
  router.patch("/:id/rechazar", requireRol(...APROBADORES), c.rechazar);
}

router.delete("/:id", requireRol(...APROBADORES), c.remove);

module.exports = router;
