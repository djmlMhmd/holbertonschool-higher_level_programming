$(document).ready(() => {
	$('DIV#add_item').click(() => {
		var liste = $('<li>Item</li>');
		$('UL.my_list').appendChild(liste);
	});
});
