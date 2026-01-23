from django.urls import path

from ex01.views import django, display, templates

urlpatterns = [
    path('django/', django, name='ex01-django'),
    path('display/', display, name='ex01-display'),
    path('templates/', templates, name='ex01-templates'),
]
