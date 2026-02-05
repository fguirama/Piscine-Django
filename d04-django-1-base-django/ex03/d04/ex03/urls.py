from django.urls import path

from ex03.views import ex03_table

urlpatterns = [
    path('', ex03_table, name='ex03'),
]
