var keys = {};

$(document).keydown(function (e) {
	keys[e.which] = true;

	var json_upload = JSON.stringify({command:keys});
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("POST", "/post");
	xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	xmlhttp.send(json_upload);

	// printKeys();
});

$(document).keyup(function (e) {
	delete keys[e.which];

	var json_upload = JSON.stringify({command:keys});
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("POST", "/post");
	xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	xmlhttp.send(json_upload);

	// printKeys();
});

// function printKeys() {
// 	var html = '';
// 	for (var i in keys) {
// 		if (!keys.hasOwnProperty(i)) continue;
// 		html += '<p>' + i + '</p>';
// 	}
// 	$('#out').html(html);
// }
