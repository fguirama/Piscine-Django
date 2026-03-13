function showNewMessage(data) {
    const $listMessages = $('<li>');

    $listMessages.addClass('d-flex');
    if (data.username) {
        $listMessages.append($('<div>').text(data.username + ':'))
    }
    $listMessages.append($('<div>').text(data.message))
    $('#messages').append($listMessages)
}

function showNewMessages(data) {
    if (data.type === 'history') {
        data.messages.forEach(message => {
            showNewMessage(message);
        })
    }
    else {
        showNewMessage(data);
    }
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

        showNewMessages(data);
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
