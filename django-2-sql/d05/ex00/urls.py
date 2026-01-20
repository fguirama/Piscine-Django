from django.urls import path

from ex00.views import ex00_init

urlpatterns = [
    path('init/', ex00_init),
]
