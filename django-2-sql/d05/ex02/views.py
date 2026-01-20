from django.shortcuts import render

from ex00.views import ex00_init
from ex02.models import instert_sql_data, get_sql_data


def ex02_init(request):
    return ex00_init(request, 2)


def ex02_populate(request):
    context = instert_sql_data()
    return render(request, 'status.html', context)


def ex02_display(request):
    data = get_sql_data()
    return render(request, 'display_movies.html', data)
