fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
	.then(function (response) {
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		return response.json();
	})
	.then(function (data) {
		var characterElement = document.getElementById('character');
		characterElement.textContent = data.name;
		console.log('Nom du personnage:', data.name);
	})
	.catch(function (error) {
		console.error('Fetch error:', error);
	});
