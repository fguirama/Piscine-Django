from django.urls import path

from ex06.views import ex06_init, ex06_populate, ex06_display, ex06_remove, ex06_update

urlpatterns = [
    path('init/', ex06_init),
    path('populate/', ex06_populate),
    path('display/', ex06_display),
    path('remove/', ex06_remove),
    path('update/', ex06_update),
]
