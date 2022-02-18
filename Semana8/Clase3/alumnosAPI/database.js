const mysql=require('mysql');

// crear conecion a base de datos

const mysqlConection=mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'password',
    database:'db_matricula'
});

mysqlConection.connect(function(err){
    if(err){
        console.log('error');
        return;
    }
    else{
        console.log('database is conected')
    }
});

module.exports=mysqlConection;