from rest_framework import viewsets
from .models import Quote
from .pagination import QuotePagination
from .serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all().order_by('-pk')
    serializer_class = QuoteSerializer
    pagination_class = QuotePagination
