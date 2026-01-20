from django.shortcuts import render

from ex00.models import create_movies_table


def ex00_init(request, exersice=0):
    context = create_movies_table(exersice)
    return render(request, 'status.html', context)
