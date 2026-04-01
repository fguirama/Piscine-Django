from django.contrib.auth.forms import AuthenticationForm


def login_form(_):
    return {'login_form': AuthenticationForm()}
