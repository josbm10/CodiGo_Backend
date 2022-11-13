const express = require('express');
const { config } = require('../config/index');
const cors = require('cors')


const app = express();

app.use(cors());

app.use(express.json());

app.get('/',(req,res)=> {
    res.json({mensaje:'Microservicio CATEGORIA a mi API punto de venta'})
})
app.use(require('../routes/categoria'));

app.listen(config.categoria.port,function(){
    console.log(`SERVIDOR http://localhost:${config.categoria.port}`);
})