from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quotes to be viewed or edited.
    """
    queryset = Quote.objects.all().order_by('-date')
    serializer_class = QuoteSerializer
