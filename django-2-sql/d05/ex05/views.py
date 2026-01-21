from django.shortcuts import render

from ex03.models import get_orm_data
from ex03.views import ex03_display, ex03_populate
from ex05.models import Movies


def ex05_populate(request):
    return ex03_populate(request, 5, Movies)


def ex05_display(request):
    return ex03_display(request, 5, Movies)


def ex05_remove(request, n=5, movies_database=Movies):
    status = None
    if request.method == 'POST':
        title = request.POST.get('movie')
        res = movies_database.objects.filter(title=title).delete()
        if res[0]:
            status = {'status': 'OK', 'text': 'Data removed successfully!'}
        else:
            status = {'status': 'KO', 'text': f'No movie found with title "{title}"'}

    data = get_orm_data(movies_database)
    return render(request, 'remove_movie.html', {**data, 'n': n, 'status': status})
