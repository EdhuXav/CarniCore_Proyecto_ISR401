const createCrudController = require("./crudFactory");
const { GuiaOrigen, Proveedor } = require("../models");

module.exports = createCrudController(GuiaOrigen, { include: [Proveedor] });
