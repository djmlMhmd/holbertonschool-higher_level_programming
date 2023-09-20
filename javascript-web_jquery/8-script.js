$(document).ready(() => {
	fetch('https://swapi-api.hbtn.io/api/films/?format=json')
		.then((r) => {
			if (!r.ok) {
				throw new Error('Network response was not ok');
			}
			return r.json();
		})
		.then((data) => {
			data.results.forEach((element) => {
				var listItem = $('<li>' + element.title + '</li>');
				$('UL#list_movies').append(listItem);
			});
		})
		.catch((error) => {
			console.error('Fetch error:', error);
		});
});
