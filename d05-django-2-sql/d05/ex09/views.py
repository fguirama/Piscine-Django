from django.shortcuts import render

from ex09.models import People


def ex09_display(request):
    command_line = 'python3 d05/manage.py loaddata d05/ex09/ex09_initial_data.json'
    peoples = People.objects.filter(homeworld__climate__icontains='windy').order_by('name').values('name', 'homeworld__name', 'homeworld__climate')
    return render(request, 'display_people.html', {'peoples': peoples, 'command_line': command_line, 'n': 9, 'data_source': 'ORM'})
