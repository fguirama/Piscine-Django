from django.shortcuts import render

from d05.sql import make_query
from ex00.models import create_movies_table


def ex00_init(request, n=0):
    context = make_query(create_movies_table, n, error='creating table')
    return render_status(request, context, n)


def render_status(request, context, n):
    return render(request, 'page_status.html', {**context, 'n': n})
