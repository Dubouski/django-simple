from django.shortcuts import render
from rest_framework import generics
from .serializers import ArticlesSerializer
from .models import Articles


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior rest api."""
    queryset = Articles.objects.all().order_by('-date')
    serializer_class = ArticlesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new article."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new article."""
        serializer.save()


def home(request):
    c = {}
    return render(request, 'core/listArticles.html', c)
