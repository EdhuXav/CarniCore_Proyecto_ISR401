const createCrudController = require("./crudFactory");
const { MovimientoInventario, ProductoAlmacenado, CamaraFrigorifica } = require("../models");
module.exports = createCrudController(MovimientoInventario, {
  include: [ProductoAlmacenado, CamaraFrigorifica],
});
