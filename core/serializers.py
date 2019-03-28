from rest_framework import serializers
from .models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Articles
        fields = ('id', 'title', 'body', 'date')
        read_only_fields = ('id', 'date')
