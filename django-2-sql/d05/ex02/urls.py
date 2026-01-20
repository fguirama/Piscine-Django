from django.urls import path

from ex02.views import ex02_init, ex02_populate, ex02_display

urlpatterns = [
    path('init/', ex02_init),
    path('populate/', ex02_populate),
    path('display/', ex02_display),
]
