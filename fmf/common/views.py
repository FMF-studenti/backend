from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
