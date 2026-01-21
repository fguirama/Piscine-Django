from django.shortcuts import render

from ex00.models import create_movies_table


def ex00_init(request, n=0):
    context = create_movies_table(n)
    return render_status(request, context, n)


def render_status(request, context, n):
    return render(request, 'status.html', {**context, 'n': n})
