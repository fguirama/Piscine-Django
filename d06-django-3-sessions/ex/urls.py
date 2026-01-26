from django.urls import path

from ex import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upvote/<int:tip_id>/', views.upvote_downvote_tip, name='upvote_tip'),
    path('downvote/<int:tip_id>/', views.upvote_downvote_tip, name='downvote_tip'),
    path('delete/<int:tip_id>/', views.delete_tip, name='delete_tip'),
]
