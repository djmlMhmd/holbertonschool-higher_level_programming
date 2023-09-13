let toggleHeaderElement = document.getElementById('toggle_header');

let headerElement = document.querySelector('header');

toggleHeaderElement.addEventListener('click', function () {
	if (headerElement.classList.contains('red')) {
		headerElement.classList.remove('red');
		headerElement.classList.add('green');
	} else {
		headerElement.classList.remove('green');
		headerElement.classList.add('red');
	}
});
