export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (typeof trueOrFalse === 'boolean') {
    if (trueOrFalse) {
      task = true;
      task2 = false;
    }
  } else {
    console.error('Paramètre invalide : un booléen est requis');
  }

  return [task, task2];
}