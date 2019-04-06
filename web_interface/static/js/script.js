var keys = {};

const makeDriveCall = () => {
	fetch('http://192.168.2.171:5001/drive', {
		method: 'POST',
		headers: new Headers({
			'Content-Type': 'application/json',
		}),
		body: JSON.stringify({
			command: keys
		})
	});
};

$(document).keydown(e => {
	keys[e.which] = true;
	makeDriveCall();
});

$(document).keyup(e => {
	delete keys[e.which];
	makeDriveCall();
});

$('#record').click(function () {
	const isRecording = $(this).val() === 'Stop Recording';
	let newVal;

	console.log('YOOOO', $(this).val());

	if (isRecording) {
		// Make API call here...
		newVal = 'Start Recording';
	} else {
		// Make API call here...
		newVal = 'Stop Recording';
	}
	$(this).attr('value', newVal);
});