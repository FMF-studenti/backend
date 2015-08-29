from rest_framework_ember.pagination import PageNumberPagination


class QuotePagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
