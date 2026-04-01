from django.contrib import admin

from articles.models import Article, UserFavouriteArticle

admin.site.register(Article)
admin.site.register(UserFavouriteArticle)
