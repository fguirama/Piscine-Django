from django.shortcuts import render

from ex09.models import People


def ex09_display(request):
    no_data_text = 'No data available, please use the following command line before use: <code>python3 manage.py loaddata people.json</code>'
    peoples = People.objects.filter(homeworld__climate__icontains='windy').order_by('name').values('name', 'homeworld__name', 'homeworld__climate')
    return render(request, 'display_people.html', {'peoples': peoples, 'no_data_text': no_data_text, 'n': 9, 'data_source': 'ORM'})
