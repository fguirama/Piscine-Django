from django.urls import path

from articles.views import ArticleListView, PublicationListView, ArticleDetailView, FavouriteListView, \
    ArticleCreateView, AddFavouriteView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:pk>/favourite/', AddFavouriteView.as_view(), name='add-favourite'),
    path('favourites/', FavouriteListView.as_view(), name='favourites'),
    path('publications/', PublicationListView.as_view(), name='publications'),
    path('publish/', ArticleCreateView.as_view(), name='publish')
]
