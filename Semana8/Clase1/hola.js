console.log('hola mundo');
let i=0;

var id=setInterval(function(){
    i++;
    if(i==5){
        clearInterval(id)
    }
    console.log(i)
},1000);
console.log('adios mundo');