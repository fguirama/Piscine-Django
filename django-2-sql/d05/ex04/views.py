from django.shortcuts import render

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


def ex04_remove(request, n=4):
    status = None
    if request.method == 'POST':
        title = request.POST.get('movie')
        print('TITLE:', title, flush=True)
        status = remove_sql_data(n, title)

    data = get_sql_data(n)
    return render(request, 'remove_movie.html', {**data, 'n': n, 'status': status})
