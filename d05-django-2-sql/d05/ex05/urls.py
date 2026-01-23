from django.urls import path

from ex05.views import ex05_populate, ex05_display, ex05_remove

urlpatterns = [
    path('populate/', ex05_populate),
    path('display/', ex05_display),
    path('remove/', ex05_remove),
]
