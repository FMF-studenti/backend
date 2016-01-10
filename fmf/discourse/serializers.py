from rest_framework import serializers
from .models import Topic, User


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'title', 'slug', 'updated',
                  'last_poster', 'last_poster_avatar')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'messages',
                  'avatar', 'administrator', 'error')
