from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def account_view(request):
    form = AuthenticationForm()
    return render(request, 'account.html', {'form': form})


@require_POST
def login_view(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return JsonResponse({
            'success': True,
            'username': user.username
        })

    errors = form.errors.as_json()
    return JsonResponse({
        'success': False,
        'errors': errors
    })


@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True})
