import re
import feedparser
from datetime import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework import viewsets
from .models import Author, BlogArticle, ExternalLink
from .serializers import AuthorSerializer, BlogArticleSerializer, ExternalLinkSerializer


def logout_view(request):
    logout(request)

    data = request.GET
    return redirect('http://localhost:4200/?' + data.urlencode())


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlogArticleSerializer

    def get_queryset(self):
        feed = feedparser.parse('http://revija.fmf.si/feed/')
        articles = []
        for entry in feed.entries:
            id_match = re.search(r'p=(\S+)', entry['id'])
            articles.append({
                'id': id_match.group(1),
                'title': entry['title'],
                'published': datetime.strptime(entry['published'], '%Y-%m-%dT%H:%M:%SZ'),
                'link': entry['link']
            })
        return articles[:6]


class ExternalLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExternalLink.objects.all()
    serializer_class = ExternalLinkSerializer
