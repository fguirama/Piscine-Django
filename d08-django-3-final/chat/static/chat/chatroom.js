function showMessage(data) {
    const $listMessages = $('<li>');

    $listMessages.addClass('d-flex');
    $listMessages.append($('<div>').text(data.username + ':'))
    $listMessages.append($('<div>').text(data.message))
    $('#messages').append($listMessages)
}

$(document).ready(function() {
    console.log('Room name:', roomName);
    const socket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');

    socket.onopen = function() {
        console.log('Connected');
    };

    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log('Message:', data);

        showMessage(data);
    };

    socket.onclose = function() {
        console.log('Disconnected');
    };

    $('#send').click(function() {
        const $message = $('#message');
        const message = $message.val();
        const data = {
            message: message,
            username: userName
        }

        $message.val('');
        socket.send(JSON.stringify(data));
        $message.focus();
    });
});
