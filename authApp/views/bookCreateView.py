from rest_framework import status, generics 
from rest_framework.response import Response
from authApp.serializers.bookSerializer import BookSerializer
from authApp.models.book import Book
from rest_framework.decorators import action

class BookCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['post'], detail=True)
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(methods=['get'], detail=True)
    def get_queryset(self):
        return Book.objects.filter()
    
