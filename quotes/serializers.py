from .models import Quote
from rest_framework import serializers


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'author', 'content', 'date', 'ip')
        extra_kwargs = {'ip': {'write_only': True}}
