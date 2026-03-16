function showNewUser(username) {
    const $user = $("#users [data-value=" + username + "]");

    if (!$user.length) {
        const $listUser = $('<li>').attr('data-value', username).text(username);
        $('#users').append($listUser)
    }
}

function removeNewUser(username) {
    const $user = $("#users [data-value=" + username + "]");
    if ($user.length) {
        $user.remove();
    }
}

function showConnectedUsers(users) {
    $('#users').empty();
    users.forEach(user => {
        showNewUser(user);
    })
}

function showNewMessage(data) {
    const $listMessages = $('<p>').addClass('chat-messages');

    if (data.type === 'user_joined') {
        showNewUser(data.username);
        $listMessages.addClass('text-success fst-italic');
        $listMessages.append($('<i>').addClass('bi bi-box-arrow-in-right me-1'));
    }
    else if (data.type === 'user_left') {
        removeNewUser(data.username);
        $listMessages.addClass('text-danger fst-italic');
        $listMessages.append($('<i>').addClass('bi bi-box-arrow-right me-1'));
    }
    else {
        $listMessages.append($('<strong>').addClass('chat-username text-primary').text(data.username + ': '))
    }
    $listMessages.append(data.message)

    const $messages = $('#messages')
    $messages.append($listMessages)
    $messages.scrollTop($messages[0].scrollHeight);
}

function showNewMessages(data) {
    if (data.type === 'connection_success') {
        data.messages.forEach(message => {
            console.log(message);
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

        if (data.type === 'connection_success') {
            showConnectedUsers(data.connected_users);
        }
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
