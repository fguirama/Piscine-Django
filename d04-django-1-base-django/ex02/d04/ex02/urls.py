from django.urls import path

from ex02.views import ex02_form

urlpatterns = [
    path('', ex02_form, name='ex02'),
]
