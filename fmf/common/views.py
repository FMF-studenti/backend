from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework import viewsets
from .models import Author, ExternalLink
from .serializers import AuthorSerializer, ExternalLinkSerializer


def logout_view(request):
    logout(request)

    data = request.GET
    return redirect('http://localhost:4200/?' + data.urlencode())


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ExternalLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExternalLink.objects.all()
    serializer_class = ExternalLinkSerializer
