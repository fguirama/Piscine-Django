from django.shortcuts import render


def django(request):
    return render_ex01(request, 'django')


def display(request):
    return render_ex01(request, 'display')


def templates(request):
    return render_ex01(request, 'templates')


def render_ex01(request, filename):
    return render(request, f'content/ex01-{filename}.html')
