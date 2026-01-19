from django.shortcuts import render


def ex03_table(request):
    return render(request, 'tables.html', _get_context())


def _get_context():
    c = _generate_gradient()
    return {'color_names': c.keys(), 'colors': zip(*c.values())}


def _generate_gradient():
    gradients = 50

    colors = {
        'black': [],
        'red': [],
        'blue': [],
        'green': [],
    }

    for i in range(gradients):
        value = int(0xFF / gradients * i)

        colors['black'].append(f'rgb({value},{value},{value})')
        colors['red'].append(f'rgb({value},0,0)')
        colors['blue'].append(f'rgb(0,0,{value})')
        colors['green'].append(f'rgb(0,{value},0)')
    return colors
