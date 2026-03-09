$(document).ready(function() {
    const socket = new WebSocket("ws://" + window.location.host + "/ws/chat/");

    socket.onopen = function() {
        console.log("Connected");
    };

    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log("Message:", data.message);
    };

    socket.onclose = function() {
        console.log("Disconnected");
    };

    $("#send").click(function() {
        const message = $("#message").val();

        socket.send(JSON.stringify({
            message: message
        }));
    });
});
