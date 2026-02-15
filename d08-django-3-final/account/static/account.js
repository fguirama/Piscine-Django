function showLogin(errors = "") {
    console.log('showLogin');
    $("#login-errors").text(errors);
    $("#login-block").show();
    $("#logged-block").hide();
}

function showLogged(username) {
    console.log('showLogged');
    $("#logged-username").text(username);
    $("#login-block").hide();
    $("#logged-block").show();
}


$(document).ready(function() {
    if (isAuthenticated) {
        showLogged($("#logged-username").text());
    } else {
        showLogin();
    }

    $("#login-form").submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/account/login/",
            type: "POST",
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    console.log('success', response);
                    showLogged(response.username);
                } else {
                    showLogin(response.errors);
                }
            }
        });
    });

    $("#logout-btn").click(function() {
        $.ajax({
            url: "/account/logout/",
            type: "POST",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(response) {
                if (response.success) {
                    showLogin();
                }
            }
        });
    });

});
