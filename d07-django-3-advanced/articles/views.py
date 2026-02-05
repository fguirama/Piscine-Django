from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from articles.models import Article, UserFavouriteArticle


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'


class PublicationListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'publications.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'


class FavouriteListView(LoginRequiredMixin, ListView):
    model = UserFavouriteArticle
    template_name = 'favourite_articles.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user)
