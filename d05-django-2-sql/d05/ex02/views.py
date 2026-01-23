from django.shortcuts import render

from d05.sql import make_query
from ex00.views import ex00_init, render_status
from ex02.models import instert_sql_data, get_sql_data


def ex02_init(request):
    return ex00_init(request, 2)


def ex02_populate(request, n=2):
    context = make_query(instert_sql_data, n, error='inserting data')
    return render_status(request, context, n)


def ex02_display(request, n=2, data_source='SQL'):
    data = make_query(get_sql_data, n, error='fetching data')
    return render(request, 'display_movies.html', {**data, 'n': n, 'data_source': data_source})
