from django.conf import settings 
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 
 
from authApp.models.book import Book 
from authApp.serializers.bookSerializer import BookSerializer 

class UserDetailView(generics.RetrieveAPIView): 
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 