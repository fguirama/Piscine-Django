from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    # context_object_name = 'articles'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
