from django.shortcuts import render

from ex10.forms import SearchForm
from ex10.models import Movies


def ex10_views(request):
    form = SearchForm(request.POST or None)
    results = []

    if form.is_valid():
        min_date = form.cleaned_data['min_release_date']
        max_date = form.cleaned_data['max_release_date']
        diameter = form.cleaned_data['planet_diameter']
        gender = form.cleaned_data['gender']

        movies = Movies.objects.filter(release_date__range=(min_date, max_date), characters__gender=gender, characters__homeworld__diameter__gte=diameter).select_related().prefetch_related('characters').distinct()

        for movie in movies:
            for character in movie.characters.filter(gender=gender, homeworld__diameter__gte=diameter):
                results.append({
                    'movie': movie.title,
                    'name': character.name,
                    'gender': character.gender,
                    'planet': character.homeworld.name,
                    'diameter': character.homeworld.diameter,
                })

    return render(request, 'ex10.html', {'form': form, 'results': results})
