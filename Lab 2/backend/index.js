const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(express.json());
app.use(cors());

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

const createRandomUser = async () => {
  const timestamp = Date.now();
  const username = `user_${timestamp}_${Math.floor(Math.random() * 10000)}`;
  const email = `user${timestamp}@example.com`;

  try {
    const result = await pool.query(
      'INSERT INTO users (username, email) VALUES ($1, $2) RETURNING *',
      [username, email]
    );
    console.log('Random user created:', result.rows[0]);
  } catch (error) {
    console.error('Error creating random user:', error);
  }
};

const initDB = async () => {
  try {
    await pool.query(`
      CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL
      )
    `);
    console.log('Users table ensured');
    await createRandomUser();
  } catch (error) {
    console.error('Error initializing database:', error);
  }
};

app.get('/', (req, res) => {
  res.send('Backend is running!');
});

// app.get('/users', async (req, res) => {
//   try {
//     const result = await pool.query('SELECT * FROM users');
//     res.json(result.rows);
//   } catch (error) {
//     console.error(error);
//     res.status(500).send('Server error');
//   }
// });

app.get('/users', async (req, res) => {
    try {
      await createRandomUser();
      const result = await pool.query('SELECT * FROM users');
      res.json(result.rows);
    } catch (error) {
      console.error(error);
      res.status(500).send('Server error');
    }
});

app.listen(port, async () => {
  console.log(`Server running on http://localhost:${port}`);
  await initDB();
});

module.exports = app;
