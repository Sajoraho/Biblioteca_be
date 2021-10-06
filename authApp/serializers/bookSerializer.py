from authApp.models.book import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'language', 'year', 'publisher', 'genre', 'number']