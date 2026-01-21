from django.shortcuts import render

from ex00.views import render_status
from ex03.models import instert_sql_data, get_sql_data


def ex03_populate(request):
    context = instert_sql_data()
    return render_status(request, context, 3)


def ex03_display(request):
    data = get_sql_data()
    return render(request, 'display_movies.html', {**data, 'n': 3})
