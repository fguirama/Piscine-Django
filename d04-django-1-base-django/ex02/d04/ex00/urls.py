from django.urls import path

from ex00.views import ex00_template

urlpatterns = [
    path('', ex00_template, name='ex00'),
]
