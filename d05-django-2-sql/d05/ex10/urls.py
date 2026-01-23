from django.urls import path

from ex10.views import ex10_views

urlpatterns = [
    path('', ex10_views),
]
