let addItem = document.getElementById(add_item);

addItem.addEventListener('click', function () {
	let newItem = document.createElement('li');
	newItem.textContent = 'Item';

	let myList = document.querySelector('.my_list');
	myList.appendChild(newItem);
});
