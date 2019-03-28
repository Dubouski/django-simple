from django.test import TestCase
from .models import Articles

from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.articles_title = "The First Title"
        self.articles_body = "Body of The First Title"
        self.articles = Articles(title=self.articles_title, body=self.articles_body)

    def test_model_can_create_a_articles(self):
        """Test the articles model can create a articles."""
        old_count = Articles.objects.count()
        self.articles.save()
        new_count = Articles.objects.count()
        self.assertNotEquals(old_count, new_count)


# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.articles_data = {'title': 'Main title', 'body': 'Main body'}
        self.response = self.client.post(
            reverse('create'),
            self.articles_data,
            format="json")

    def test_api_can_create_a_article(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
