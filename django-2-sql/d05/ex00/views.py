from django.shortcuts import render

from ex00.models import create_movies_table


def ex00_view(request):
    context = create_movies_table()
    return render(request, 'create_sql.html', context)
