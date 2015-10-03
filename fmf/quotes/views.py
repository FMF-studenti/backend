from rest_framework import viewsets
from .models import Quote
from .pagination import QuotePagination
from .serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    pagination_class = QuotePagination

    def get_queryset(self):
        params = dict(self.request.GET)
        if 'random' in params.keys() and 'true' in params['random']:
            sort = '?'
        else:
            sort = '-pk'

        return Quote.objects.all().order_by(sort)
