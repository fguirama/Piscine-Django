function showMessage(data) {
    const $listMessages = $('<li>');

    if (data.username) {
        $listMessages.addClass('d-flex');
        $listMessages.append($('<div>').text(data.username + ':'))
        $listMessages.append($('<div>').text(data.message))
    }
    else {
        $listMessages.text(data.message)
    }
    $('#messages').append($listMessages)
}



$(document).ready(function() {
    function sendMessage() {
        const $message = $('#message');
        const message = $message.val();
        const data = {
            message: message,
            username: userName
        }

        $message.val('');
        socket.send(JSON.stringify(data));
        $message.focus();
    }

    const socket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');

    socket.onopen = function() {
        console.log('Connected');
    };

    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);

        showMessage(data);
    };

    socket.onclose = function() {
        console.log('Disconnected');
    };

    $('#message').on('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });

    $('#send').click(function() {
        sendMessage();
    });
});
