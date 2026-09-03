const router = require("express").Router();
const c = require("../controllers/usuarioController");
const { requireRol, requireNivelMinimo } = require("../middlewares/roles");

/**
 * Control de acceso por rol (auditoria del 2026-09-03).
 *
 * Antes, cualquier usuario autenticado --incluido el rol carnicero-- podia
 * listar, crear, editar y BORRAR usuarios. Ahora la gestion de usuarios queda
 * restringida, conforme al RF-15.
 */

const GESTORES = ["propietaria", "administrador_general"];

router.get("/", requireNivelMinimo("encargado_bodega"), c.getAll);
router.get("/:id", requireNivelMinimo("encargado_bodega"), c.getById);

router.post("/", requireRol(...GESTORES), c.create);
router.put("/:id", requireRol(...GESTORES), c.update);

// Cada persona puede cambiar su propia contrasena; el control fino esta en el
// controlador, que compara req.user.id con el id de la ruta.
router.patch("/:id/password", c.cambiarPassword);

router.patch("/:id/desactivar", requireRol(...GESTORES), c.desactivar); // RF-15
router.patch("/:id/activar", requireRol(...GESTORES), c.activar);

// El borrado fisico de un usuario destruye la trazabilidad de sus acciones.
// Se reserva a la propietaria; la via ordinaria es desactivar.
router.delete("/:id", requireRol("propietaria"), c.remove);

module.exports = router;
