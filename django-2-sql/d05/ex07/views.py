from django.shortcuts import render

from ex03.models import get_orm_data
from ex03.views import ex03_display, ex03_populate
from ex05.views import ex05_remove
from ex07.models import Movies


def ex07_populate(request):
    return ex03_populate(request, 7, Movies)


def ex07_display(request):
    return ex03_display(request, 7, Movies)


def ex07_remove(request):
    return ex05_remove(request, 7, Movies)


def ex07_update(request, n=7, movies_database=Movies, data_source='ORM'):
    status = None
    if request.method == 'POST':
        title = request.POST.get('movie')
        opening_crawl = request.POST.get('opening_crawl')
        res = movies_database.objects.filter(title=title).update(opening_crawl=opening_crawl)
        if res:
            status = {'status': 'OK', 'text': 'Data removed successfully!'}
        else:
            status = {'status': 'KO', 'text': f'No movie found with title "{title}"'}

    data = get_orm_data(movies_database)
    return render(request, 'update_movies.html', {**data, 'n': n, 'data_source': data_source, 'status': status})
