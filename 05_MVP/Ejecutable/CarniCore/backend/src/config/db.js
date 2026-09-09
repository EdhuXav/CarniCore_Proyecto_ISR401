const { Sequelize } = require("sequelize");

const {
  DB_HOST = "postgres",
  DB_PORT = 5432,
  DB_NAME = "carnicore",
  DB_USER = "carnicore_user",
  DB_PASSWORD = "carnicore_pass",
} = process.env;

const sequelize = new Sequelize(DB_NAME, DB_USER, DB_PASSWORD, {
  host: DB_HOST,
  port: DB_PORT,
  dialect: "postgres",
  logging: false,
  define: {
    underscored: true,
    timestamps: true,
  },
});

module.exports = sequelize;
