$(document).ready(() => {
	$('DIV#toggle_header').click(() => {
		var header = $('header');
		if (header.hasClass('red')) {
			header.removeClass('red');
			header.addClass('green');
		} else {
			header.removeClass('green');
			header.addClass('red');
		}
	});
});
