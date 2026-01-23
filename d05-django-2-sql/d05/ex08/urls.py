from django.urls import path

from ex08.views import ex08_init, ex08_populate, ex08_display

urlpatterns = [
    path('init/', ex08_init),
    path('populate/', ex08_populate),
    path('display/', ex08_display),
]
