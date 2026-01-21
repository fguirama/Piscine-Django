from django.shortcuts import render

from d05.sql import make_query
from ex00.views import render_status
from ex08.models import create_planets_table, create_people_table, instert_sql_data, get_sql_data


def ex08_init(request):
    context = {
        'statuses': [
            make_query(create_planets_table, 8, error='creating table'),
            make_query(create_people_table, 8, error='creating table')
        ]
    }
    return render_status(request, context, 8)


def ex08_populate(request):
    planets = make_query(instert_sql_data, 8, error='inserting data', name='planets', columns=['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'])
    peoples = make_query(instert_sql_data, 8, error='inserting data', name='people', columns=['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'])
    return render_status(request, {'statuses': [planets, peoples]}, 8)


def ex08_display(request, n=8, data_source='SQL'):
    data = make_query(get_sql_data, n, error='fetching data')
    print('DATA', data, flush=True)
    return render(request, 'display_people.html', {**data, 'n': n, 'data_source': data_source})
