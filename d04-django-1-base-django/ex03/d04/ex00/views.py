from django.shortcuts import render


def ex00_template(request):
    return render(request, 'index.html')
