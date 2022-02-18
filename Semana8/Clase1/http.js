const http=require('http')

http.createServer(function(req,res){
console.log('servidor levantado');

console.log(req.url);
switch(req.url){
    case '/hola':
        res.write('<>Hola mundo<>');
        res.end();
        break;
    default:
        res.write('<h1>Error</h1>');
        res.end();
}
}).listen(5000);

