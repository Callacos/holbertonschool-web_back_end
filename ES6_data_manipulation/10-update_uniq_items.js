export default function updateUniqueItems(articles) {
  if (!(articles instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [item, quantity] of articles) {
    if (quantity === 1) {
      articles.set(item, 100);
    }
  }
}
