from django.shortcuts import render

from ex03.models import instert_sql_data, get_sql_data


def ex03_populate(request):
    context = instert_sql_data()
    return render(request, 'status.html', context)


def ex03_display(request):
    data = get_sql_data()
    print(data)
    return render(request, 'display_movies.html', data)
