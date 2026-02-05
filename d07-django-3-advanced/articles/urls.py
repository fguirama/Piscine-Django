from django.urls import path

from articles.views import ArticleListView, PublicationListView, ArticleDetailView, FavouriteListView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('publications/', PublicationListView.as_view(), name='publications'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('favourites/', FavouriteListView.as_view(), name='favourites')
]
