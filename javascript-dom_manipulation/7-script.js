fetch('https://swapi-api.hbtn.io/api/films/?format=json')
	.then((r) => {
		if (!r.ok) {
			throw new Error('Network response was not ok');
		}
		return r.json();
	})
	.then((data) => {
		var listMovies = document.getElementById('list_movies');
		data.results.forEach((element) => {
			var listItem = document.createElement('li');
			listItem.textContent = element.title;
			listMovies.appendChild(listItem);
		});
	})
	.catch((error) => {
		console.error('Fetch error', error);
	});
