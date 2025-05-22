const express = require('express');
const fs = require('fs');

const databaseFile = process.argv[2];
const app = express();

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').filter((line) => line);
      const students = lines.slice(1).map((line) => line.split(','));
      const fields = {};

      for (const student of students) {
        const field = student[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(student[0]);
      }

      let response = `Number of students: ${students.length}`;
      for (const [field, names] of Object.entries(fields)) {
        response += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      }

      resolve(response);
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const result = await countStudents(databaseFile);
    res.type('text').send(`This is the list of our students\n${result}`);
  } catch (err) {
    res.type('text').send(`This is the list of our students\n${err.message}`);
  }
});

app.listen(1245);

module.exports = app;
