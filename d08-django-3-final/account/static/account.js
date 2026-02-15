function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie_values = cookies[i].split('=');
            if (cookie_values[0].trim() === name) {
                cookieValue = cookie_values[1].trim();
                break;
            }
        }
    }
    return cookieValue;
}

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
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function(response) {
                if (response.success) {
                    showLogin();
                }
            }
        });
    });
});
