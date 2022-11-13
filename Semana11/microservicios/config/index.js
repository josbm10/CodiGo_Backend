require('dotenv').config();

const config = {
    port: process.env.PORT,
    dbUser: process.env.DBUSER,
    dbHost: process.env.DBHOST,
    dbPassword: process.env.DBPASSWORD,
    dbDatabase: process.env.DBDATABASE,
    secret_key: process.env.DBDATABASE,
    categoria:{
        port:process.env.CATEGORIA_PORT
    },
    mesa:{
        port:process.env.MESA_PORT
    }

}

module.exports = {config};