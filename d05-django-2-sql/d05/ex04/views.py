from django.shortcuts import render

from d05.sql import make_query
from ex00.views import ex00_init
from ex02.models import get_sql_data
from ex02.views import ex02_populate, ex02_display
from ex04.models import remove_sql_data


def ex04_init(request):
    return ex00_init(request, 4)


def ex04_populate(request):
    return ex02_populate(request, 4)


def ex04_display(request):
    return ex02_display(request, 4)


def ex04_remove(request, n=4, data_source='SQL'):
    status = None
    if request.method == 'POST':
        title = request.POST.get('movie')
        status = make_query(remove_sql_data, n, error='removing data', title=title)

    data = make_query(get_sql_data, n, error='fetching data')
    return render(request, 'remove_movie.html', {**data, 'n': n, 'data_source': data_source, 'status': status})
