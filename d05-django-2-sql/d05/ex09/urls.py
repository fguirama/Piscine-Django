from django.urls import path

from ex09.views import ex09_display

urlpatterns = [
    path('display/', ex09_display),
]
