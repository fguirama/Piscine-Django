from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from articles.models import Article, UserFavouriteArticle


class FavouritesViewAccessTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
    def test_favourites_view_accessible_only_to_logged_in_users(self):
        response = self.client.get(reverse('favourites'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
        
    def test_favourites_view_accessible_to_logged_in_users(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('favourites'))
        self.assertEqual(response.status_code, 200)
        
    def test_favourites_template_accessible_only_to_logged_in_users(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('favourites'))
        self.assertTemplateUsed(response, 'favourite_articles.html')


class PublicationsViewAccessTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
    def test_publications_view_accessible_only_to_logged_in_users(self):
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
        
    def test_publications_view_accessible_to_logged_in_users(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 200)
        
    def test_publications_template_accessible_only_to_logged_in_users(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('publications'))
        self.assertTemplateUsed(response, 'publications.html')


class PublishViewAccessTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
    def test_publish_view_accessible_only_to_logged_in_users(self):
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
        
    def test_publish_view_accessible_to_logged_in_users(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 200)
        
    def test_publish_template_accessible_only_to_logged_in_users(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('publish'))
        self.assertTemplateUsed(response, 'publish_article.html')


class RegisterViewAccessTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
    def test_user_logged_in_cannot_access_registration_form(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 302)
        
    def test_user_not_logged_in_can_access_the_registration_form(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)


class DuplicateFavouriteTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.article = Article.objects.create(title='Test Article', author=self.user, synopsis='Test synopsis', content='Test content')
        
    def user_cannot_add_the_same_article_to_favourites_twice(self):
        self.client.login(username='testuser', password='testpass123')

        response = self.client.post(reverse('add-favourite', kwargs={'pk': self.article.pk}))
        self.assertEqual(UserFavouriteArticle.objects.filter(user=self.user, article=self.article).count(), 1)

        response = self.client.post(reverse('add-favourite', kwargs={'pk': self.article.pk}))
        self.assertEqual(UserFavouriteArticle.objects.filter(user=self.user, article=self.article).count(), 1)
