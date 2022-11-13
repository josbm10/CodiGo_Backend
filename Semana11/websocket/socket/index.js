const express=require('express')
const app=express()

app.set('port',process.env.PORT||5000)



/************** levantando archivos estaticos ******/
const path = require('path')
app.use(express.static(path.join(__dirname,'public')))

const server=app.listen(app.get('port'),()=>{
    console.log(`Corriendo en http://localhost:${app.get('port')} `)
})


//####### web socket ######
const SocketIO=require('socket.io')
const io =SocketIO(server);

io.on('connection',(socket)=>{
console.log('nueva conection wesocket: ',socket.id)
socket.on('mensajeCliente',(data)=>{
    console.log('mensaje de cliente :',data);
    io.sockets.emit('mensajeServidor',data)
})
socket.on('usuario',(usu)=>{
    console.log('mensaje de usuario :',usu);
    io.sockets.emit('mensajeServidor',usu)
})
})