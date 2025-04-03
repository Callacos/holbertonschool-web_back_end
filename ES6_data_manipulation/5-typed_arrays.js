export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range'); // Lève une erreur si la position est hors limite
  }

  const buffer = new ArrayBuffer(length); // Crée un buffer de taille "length"
  const view = new DataView(buffer); // Crée une vue DataView pour manipuler le buffer

  view.setInt8(position, value); // Place la valeur à la position spécifiée

  return view; // Retourne la vue DataView
}
