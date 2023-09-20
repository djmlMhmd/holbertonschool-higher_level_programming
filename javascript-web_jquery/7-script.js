$(document).ready(() => {
	fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
		.then((r) => {
			if (!r.ok) {
				throw new Error('Network response was not ok');
			}
			return r.json();
		})
		.then((data) => {
			$('DIV#character').text('Nom du personnage : ' + data.name);
		})
		.catch((error) => {
			console.error('Fetch error:', error);
		});
});
