const fs = require('fs').promises;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8')
      .then((data) => {
        const lines = data
          .split('\n')
          .filter((line) => line.trim() !== '');

        const students = lines.slice(1);
        console.log(`Number of students: ${students.length}`);

        const fields = {};
        for (const student of students) {
          const parts = student.split(',');
          const firstname = parts[0];
          const field = parts[parts.length - 1];

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }

        for (const field in fields) {
          const list = fields[field];
          console.log(
            `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
          );
        }

        resolve();
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
}

module.exports = countStudents;
