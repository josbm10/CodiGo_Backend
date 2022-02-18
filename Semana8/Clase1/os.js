// trabajndo con el sistema operativo

const os=require('os');

console.log(os.arch());
console.log(os.platform());
console.log(os.cpus().length);
console.log(os.totalmem());

// const tam=1024;
// function kb(bytes){return bytes/tam}
// function mb(bytes){return kb(bytes)/tam}
// function gb(bytes){return mb(bytes)/tam}
// console.log('memoria ram',gb(os.totalmem()))

let factor=1024
async function memoria(bytes){
        return new Promise(function(resolve,reject){
                    result=bytes/factor
                    resolve(result)
            }) }
async function main(){
    setTimeout(async function(){
        console.log('memoria usando async await')
       kb= await memoria(os.totalmem())
       mb= await memoria(kb)
       gb= await memoria(mb)
        console.table([ {capacidad:'kb',tam:kb},
                        {capacidad:'mb',tam:mb},
                        {capacidad:'gb',tam:gb}
                    ])
        },2000)}
main()
            