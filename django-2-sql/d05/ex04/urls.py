from django.urls import path

from ex04.views import ex04_init, ex04_populate, ex04_display, ex04_remove

urlpatterns = [
    path('init/', ex04_init),
    path('populate/', ex04_populate),
    path('display/', ex04_display),
    path('remove/', ex04_remove),
]
