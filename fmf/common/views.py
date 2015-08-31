from rest_framework import viewsets
from .models import Author, ExternalLink
from .serializers import AuthorSerializer, ExternalLinkSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ExternalLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExternalLink.objects.all()
    serializer_class = ExternalLinkSerializer
