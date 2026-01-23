from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ex.forms import SignupForm, LoginForm, TipsForm
from ex.models import Tip


def index_view(request):
    form = None
    tips = Tip.objects.select_related('author').order_by('-date')

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TipsForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.author = request.user
                tip.save()
                return redirect('home')
        else:
            form = TipsForm()
    return render(request, 'home.html', {'tips': tips, 'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        login(request, form.user)
        return redirect('home')

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = SignupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html', {'form': form})
