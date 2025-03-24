export function taskFirst() {
	const task = 'I prefer const when I can.'; // Remplace var par const
	return task;
  }
  
  export function getLast() {
	return ' is okay';
  }
  
  export function taskNext() {
	let combination = 'But sometimes let'; // Remplace var par let
	combination += getLast();
  
	return combination;
  }
  