function countStudents(filePath) {
  const fs = require('fs');
    let content;
  try {
    content = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  const lines = content.split('\n').filter(line => line.trim() !== '');
  const students = lines.slice(1); // sans l'en-tête
  console.log(`Number of students: ${students.length}`);
  const fields = {};

  for (const student of students) {
    const parts = student.split(',');
    const firstName = parts[0];
    const field = parts[parts.length - 1];

    if (!fields[field]) {
      fields[field] = [];
    }

    fields[field].push(firstName);
  }
    for (const field in fields) {
      const list = fields[field].join(', ');
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
    }
  }
