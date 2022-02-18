const express = require("express");
const app = express();

//Settings
app.set("port", process.env.PORT || 5000);

//Middlewares
app.use(express.json());

//Server
app.listen(app.get("port"), () => {
    console.log(`Server running at http://localhost:${app.get("port")}`);
  });
  
//Routes
const mysqlConection = require("./database");

app.get("/alumnos", function (req, res) {
    mysqlConection.query("select * from tbl_alumno", (err, rows, fields) => {
      if (!err) {
        res.json(rows);
      } 
      else {
        console.log(err);
      }
    });
  });

app.post("/alumnos", function (req, res) {
  
    const{alumno_nombre,alumno_email}=req.body;
    const query ='insert into tbl_alumno(alumno_nombre,alumno_email) values(?,?)';
    mysqlConection.query(query,[alumno_nombre,alumno_email], (err, rows, fields) => {
      if (!err) {
        res.json({'status':true,
                  'content':'employed inserted'});
      } 
      else {
        console.log(err);
      }
    });
  });

app.put("/alumnos/:alumno_id", function (req, res) {

    const{alumno_nombre,alumno_email}=req.body;
    const {alumno_id}=req.params;
    const query ='update tbl_alumno set alumno_nombre=?,alumno_email=? where alumno_id=?';
    mysqlConection.query(query,[alumno_nombre,alumno_email,alumno_id], (err, rows, fields) => {
      if (!err) {
        res.json({'status':true,
                  'content':'employed updated'});
      } 
      else {
        console.log(err);
      }
    });
  });
  
app.delete("/alumnos/:alumno_id", function (req, res) {
  
    const {id}=req.params;
    const query ='delete from tbl_alumno where alumno_id=?';
    mysqlConection.query(query,[id], (err, rows, fields) => {
      if (!err) {
        res.json({'status':true,
                  'content':'employed deleted'});
      } 
      else {
        console.log(err);
      }
    });
  });