var keys = {};

const BASE_API_URL = 'http://192.168.2.171:5001';
const makeDriveCall = () => {
  fetch(`${BASE_API_URL}/drive`, {
    method: 'POST',
    headers: new Headers({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify({command: keys})
  });
};

$(document).ready(() => {
  $(document).keydown(e => {
    keys[e.which] = true;
    makeDriveCall();
  });

  $(document).keyup(e => {
    delete keys[e.which];
    makeDriveCall();
  });

  $('#record').click(function() {
    let newVal, apiUrl;

    if ($(this).val() === 'Stop Recording') {
      newVal = 'Start Recording';
      apiUrl = 'stop_recording';
    } else {
      newVal = 'Stop Recording';
      apiUrl = 'start_recording';
    }

    $(this).val(newVal);
    fetch(`${BASE_API_URL}/${apiUrl}`, {method: 'POST'});
  });
});