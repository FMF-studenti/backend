from rest_framework import serializers
from .models import Author, BlogArticle, ExternalLink


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'contribution', 'active')


class BlogArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogArticle
        fields = ('id', 'title', 'published', 'link')


class ExternalLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExternalLink
        fields = ('id', 'title', 'url')
