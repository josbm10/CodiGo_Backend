const express = require('express');
const { config } = require('../config/index');
const cors = require('cors')


const app = express();

app.use(cors());

app.use(express.json());

app.get('/',(req,res)=> {
    res.json({mensaje:'Microservicio MESA  a mi API punto de venta'})
})
app.use(require('../routes/mesa'));

app.listen(config.mesa.port,function(){
    console.log(`SERVIDOR http://localhost:${config.mesa.port}`);
})