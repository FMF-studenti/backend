from random import choice
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import Quote
from .pagination import QuotePagination
from .serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all().order_by('-pk')
    serializer_class = QuoteSerializer
    pagination_class = QuotePagination

    @list_route()
    def latest_and_random(self, request):
        latest = Quote.objects.latest('pk')
        random = choice(Quote.objects.all())

        serializer = self.get_serializer([latest, random], many=True)
        return Response(serializer.data)
