const express = require('express');
const app = express();
const port = 3000;


app.get('/', (req, res) => {
  const data = {
    Instancia: "Instancia #2 - API #2",
    Curso: "Seminario de Sistemas 1",
    Estudiante: "Estudiante - 201901055"
  };
  res.json(data);
});

app.get('/check', (req, res) => {
  res.status(200).json({status:'OK'})
});


app.listen(port, () => {
  console.log(`Servidor en http://localhost:${port}`);
});