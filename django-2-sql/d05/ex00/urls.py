from django.urls import path

from ex00.views import ex00_view

urlpatterns = [
    path('init/', ex00_view),
]
