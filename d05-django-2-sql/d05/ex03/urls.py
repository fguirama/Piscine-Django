from django.urls import path

from ex03.views import ex03_populate, ex03_display

urlpatterns = [
    path('populate/', ex03_populate),
    path('display/', ex03_display),
]
