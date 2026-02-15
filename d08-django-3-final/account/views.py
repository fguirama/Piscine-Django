from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def account_view(request):
    return render(request, 'account.html')


@require_POST
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        return JsonResponse({
            'success': False,
            'errors': 'Username and password required.'
        })

    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse({
            'success': False,
            'errors': 'Invalid credentials.'
        })

    login(request, user)

    return JsonResponse({'success': True, 'username': user.username})


@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True})
