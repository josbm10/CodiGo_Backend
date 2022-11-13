const socket=io('http://localhost:5000')

let output=document.getElementById('output')
let mensaje=document.getElementById('mensaje')
let btn=document.getElementById('enviar')

socket.on('mensajeServidor',function(data){
    console.log(data)
output.innerHTML += `<p>${data.mensaje}</p>`
})

btn.addEventListener('click',()=>{
    console.log(mensaje.value)
    socket.emit('mensajeCliente',{
        mensaje:mensaje.value
    })
})
