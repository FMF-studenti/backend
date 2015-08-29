from django.http import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .api import discourse
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        user = discourse.user_info(self.request)
        return [user]

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        required = self.kwargs[lookup_url_kwarg]

        if required != 'me':
            raise Http404

        user = discourse.user_info(self.request)

        return user
