from django.conf import settings 
from rest_framework import generics
from rest_framework.response import Response 
 
from authApp.models.book import Book 
from authApp.serializers.bookSerializer import BookSerializer 

class BookDetailView(generics.RetrieveDestroyAPIView): 
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 