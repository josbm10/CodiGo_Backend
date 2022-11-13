const express = require("express");
const app = express();

const {config}=require('./config')

app.get("/", function (req, res) {
    res.json({
      'status': true,
      'content': 'servidor corriendo',
    });
  });

app.listen(config.port, () => {
    console.log(`Server running at http://localhost:${config.port}`);
  });