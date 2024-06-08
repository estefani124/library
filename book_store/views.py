

# Create your views here.
from rest_framework import viewsets,permissions
from.models import Genre, Author, Book, BookAuthor
from.serializer import GenreSerializer, AuthorSerializer, BookSerializer, BookAuthorSerializer
from rest_framework.permissions import IsAuthenticated
#Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset= Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes =[IsAuthenticated]
        return[permission() for permission in permission_classes]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes =[IsAuthenticated]
        return[permission() for permission in permission_classes]   


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes =[IsAuthenticated]
        return[permission() for permission in permission_classes]

class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset= BookAuthor.objects.all()
    serializer_class =BookAuthorSerializer
    
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes =[IsAuthenticated]
        return[permission() for permission in permission_classes]
