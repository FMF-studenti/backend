from rest_framework import serializers
from .models import Quote


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'author', 'content', 'date', 'ip')
        extra_kwargs = {'ip': {'write_only': True}}
