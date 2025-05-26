const express = require('express');

const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.json({ message: "GET response"})
});

app.get('/health', (req, res) => {
    res.json({ status: "OK"})
});

module.exports = app;

if (require.main === module) {
  app.listen(port, () => {
    console.log(`REST app listening on port ${port}`);
  });
}
