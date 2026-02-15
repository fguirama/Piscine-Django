from django.urls import path

from account.views import account_views

urlpatterns = [
    path('account/', account_views),
]
