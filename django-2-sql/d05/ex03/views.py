from django.shortcuts import render

from ex00.views import render_status
from ex03.models import instert_orm_data, get_orm_data, Movies


def ex03_populate(request, n=3, movies_database=Movies):
    context = instert_orm_data(movies_database)
    return render_status(request, context, n)


def ex03_display(request, n=3, movies_database=Movies):
    data = get_orm_data(movies_database)
    return render(request, 'display_movies.html', {**data, 'n': n})
