function hola(nombre){
return new Promise(function(resolve,reject){
    setTimeout(function(){
        console.log('hola',nombre)
        resolve(nombre)
        reject('error')
    },1000)
})
}
function hablar(nombre){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            console.log('como te va',nombre)
            resolve(nombre)
            reject('error')
        },1000)
    })
    }

function adios(nombre){
        return new Promise(function(resolve,reject){
            setTimeout(function(){
                console.log('adios',nombre)
                resolve(nombre)
                reject('error')
            },1000)
        })
        }
        
hola('esthefano')
.then(hablar)
.then(adios)
.then(()=>{
    console.log('fin...')
})