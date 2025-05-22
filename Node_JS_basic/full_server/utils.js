import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').filter((line) => line);
      const students = lines.slice(1).map((line) => line.split(','));
      const result = {};

      for (const student of students) {
        const field = student[3];
        const firstName = student[0];
        if (!result[field]) result[field] = [];
        result[field].push(firstName);
      }

      resolve(result);
    });
  });
}
