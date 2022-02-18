 async function hola(nombre){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            console.log('hola',nombre)
            resolve(nombre)
            reject('error')
        },1000)
    })
    }
async function hablar(nombre){
        return new Promise(function(resolve,reject){
            setTimeout(function(){
                console.log('como te va',nombre)
                resolve(nombre)
                reject('error')
            },1000)
        })
        }
    
async function adios(nombre){
            return new Promise(function(resolve,reject){
                setTimeout(function(){
                    console.log('adios',nombre)
                    resolve(nombre)
                    reject('error')
                },1000)
            })
            }
async function main(){
    let nombre=await hola('jose')
    await hablar(nombre)
    await adios(nombre)
    console.log('fin...')

}

console.log('inicio')
main()
console.log('primero')