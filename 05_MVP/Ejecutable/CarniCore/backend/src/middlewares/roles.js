/**
 * Control de acceso por rol.
 *
 * POR QUE SE ANADE (auditoria del 2026-09-03)
 * -------------------------------------------
 * routes/index.js aplicaba requireAuth a todas las rutas --correcto-- pero no
 * habia NI UNA sola comprobacion de rol en todo el backend. El JWT transporta
 * el rol en su payload y nunca se consultaba.
 *
 * Consecuencia verificada por lectura de codigo: un usuario con rol
 * "carnicero" podia crear administradores, borrar usuarios
 * (DELETE /api/usuarios/:id) y, a traves de update() --que pasaba req.body
 * entero a item.update()--, cambiar su propio rol a "propietaria".
 *
 * Eso contradice de frente al RF-15 ("asignandoles uno de los roles
 * definidos") y al RF-09 ("con aprobacion del administrador general"), que la
 * matriz de trazabilidad da por realizados. Si el tribunal prueba el MVP
 * contra la matriz, se ve.
 */

/** Jerarquia de roles. Un rol incluye las capacidades de los inferiores. */
const JERARQUIA = {
  propietaria: 4,
  administrador_general: 3,
  encargado_bodega: 2,
  carnicero: 1,
};

/**
 * Exige que el usuario tenga uno de los roles indicados.
 *   router.post("/", requireRol("propietaria", "administrador_general"), c.create)
 */
function requireRol(...rolesPermitidos) {
  return function (req, res, next) {
    if (!req.user || !req.user.rol) {
      return res.status(401).json({ error: "Token de autenticación requerido." });
    }
    if (!rolesPermitidos.includes(req.user.rol)) {
      return res.status(403).json({
        error: "No tiene permisos suficientes para realizar esta operación.",
        rol_requerido: rolesPermitidos,
      });
    }
    return next();
  };
}

/**
 * Exige un nivel minimo en la jerarquia.
 *   router.delete("/:id", requireNivelMinimo("administrador_general"), c.remove)
 */
function requireNivelMinimo(rolMinimo) {
  const minimo = JERARQUIA[rolMinimo];
  if (minimo === undefined) {
    throw new Error(`Rol desconocido en requireNivelMinimo: ${rolMinimo}`);
  }
  return function (req, res, next) {
    if (!req.user || !req.user.rol) {
      return res.status(401).json({ error: "Token de autenticación requerido." });
    }
    if ((JERARQUIA[req.user.rol] || 0) < minimo) {
      return res.status(403).json({
        error: "No tiene permisos suficientes para realizar esta operación.",
        nivel_requerido: rolMinimo,
      });
    }
    return next();
  };
}

module.exports = { requireRol, requireNivelMinimo, JERARQUIA };
