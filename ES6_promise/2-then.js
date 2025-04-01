export default function handleResponseFromAPI(promise) {
	  return promise
	.then((response) => {
	  const { status, body } = response;
	  return {
		status: 200,
		body: 'Success',
	  };
	})
	.catch(() => new Error('The fake API is not working currently'))
	.finally(() => {
	  console.log('Got a response from the API');
	});
}