const express=require('express')

const app=express()
const port=5000

app.get('/',(req,res)=>{
res.send('<center><h1>Hola mundo express,Leonel Briceño</h1></center>')
})
app.get('/json',(req,res)=>{
    res.json({
        nombre:'Leonel Briceño',
        email:'Leonel@gmail.com'
    })
    })

app.get('/saludar/:nombre',(req,res)=>{
        res.send("hola "+req.params.nombre)
        })

app.get('/formulario/',(req,res)=>{

    html="<form action='http://localhost:5000/saludopost' method='POST'>"
    html+="<input type='text' name='nombre'/>"
    html+="<input type='submit' name='saludar'/>"
    html+="</form>"
    res.send(html)
    })

const bodyParser=require('body-parser');
app.use(bodyParser.urlencoded({ extended:true }));

app.post('/saludopost',function(req,res){
    html="<h1>Hola como estas "+ req.body.nombre +"</h1>"
    res.send(html)
    })

//######## utilizando json
app.use(express.json())
app.post('/saludopostJSON',function(req,res){
    const nombre=req.body.nombre;

    res.json({
        'saludo':'hola '+ nombre
    })
    })

app.listen(port,function(){
    console.log('servidor corriendo en http://localhost:'+ port)
})