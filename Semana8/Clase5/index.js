const express = require("express");
const app = express();

const {config}=require('./config')

const alumnosApi=require('./routes/alumnos');

app.use(express.json());

app.get("/", function (req, res) {
    res.json({
      'status': true,
      'content': 'servidor corriendo',
    });
  });

alumnosApi(app);

app.listen(config.port, () => {
    console.log(`Server running at http://localhost:${config.port}`);
  });