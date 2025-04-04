export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string' || startString === '') {
    return '';
  }

  let string = '';
  for (const i of set) {
    if (typeof i === 'string' && i.startsWith(startString)) {
      const Sub = i.substring(startString.length);
      if (Sub) {
        string += `${Sub}-`;
      }
    }
  }
  return string.slice(0, -1);
}
