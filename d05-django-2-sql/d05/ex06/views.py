from django.shortcuts import render

from d05.sql import make_query
from ex00.views import ex00_init
from ex02.models import get_sql_data
from ex02.views import ex02_populate, ex02_display

from ex04.views import ex04_remove
from ex06.models import update_sql_data


def ex06_init(request):
    return ex00_init(request, 6)


def ex06_populate(request):
    return ex02_populate(request, 6)


def ex06_display(request):
    return ex02_display(request, 6)


def ex06_remove(request):
    return ex04_remove(request, 6)


def ex06_update(request, n=6, data_source='SQL'):
    status = None
    if request.method == 'POST':
        title = request.POST.get('movie')
        opening_crawl = request.POST.get('opening_crawl')
        status = make_query(update_sql_data, n, error='updating data', title=title, opening_crawl=opening_crawl)
    data = make_query(get_sql_data, n, error='fetching data')
    return render(request, 'update_movies.html', {**data, 'n': n, 'data_source': data_source, 'status': status})
