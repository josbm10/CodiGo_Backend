// un callback es una funcion que es pasada como parametro a otra funcion

// function hola(nombre,funcion){
// setTimeout(function(){
//     console.log("hola",nombre);
//     funcion(nombre);
// },1000)
// }

// hola('jose',function(nombre){
//     console.log('adios',nombre)
// })

function hola(nombre,primercallback){
    setTimeout(function(){
        console.log("hola",nombre);
        primercallback(nombre);
    },1000)
    }
function hablar(nombre,segundocallback){
        setTimeout(function(){
            console.log("como estas",nombre);
            segundocallback(nombre);
    },1000)
    }
function adios(nombre,tercercallback){
        setTimeout(function(){
        console.log("adios",nombre);
        tercercallback(nombre);
    },1000)
    }

hola('jose',function(nombre){
    hablar(nombre,function(nombre){
        adios(nombre,function(nombre){
            console.log('fin....')
        })

    })
})