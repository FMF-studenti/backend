from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows quotes to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
