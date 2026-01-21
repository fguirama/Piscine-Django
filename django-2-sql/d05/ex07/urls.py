from django.urls import path

from ex07.views import ex07_populate, ex07_display, ex07_remove, ex07_update

urlpatterns = [
    path('populate/', ex07_populate),
    path('display/', ex07_display),
    path('remove/', ex07_remove),
    path('update/', ex07_update),
]
