const createCrudController = require("./crudFactory");
const { CamaraFrigorifica, ProductoAlmacenado } = require("../models");
module.exports = createCrudController(CamaraFrigorifica, { include: [ProductoAlmacenado] });
