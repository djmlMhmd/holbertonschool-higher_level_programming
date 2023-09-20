$(document).ready(() => {
	fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
		.then((r) => {
			if (!r.ok) {
				throw new Error('Network response was not ok');
			}
			return r.json();
		})
		.then((data) => {
			$('DIV#hello').text(data.hello);
		})
		.catch((error) => {
			console.error('Fetch error', error);
		});
});
