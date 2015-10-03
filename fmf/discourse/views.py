from django.http import Http404, JsonResponse
from rest_framework import views, viewsets
from rest_framework.permissions import IsAuthenticated
from .api import discourse
from .serializers import TopicSerializer, UserSerializer


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TopicSerializer

    def get_queryset(self):
        topics = discourse.latest_topics(self.request)
        return topics


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


class UserLogoutView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return JsonResponse(discourse.user_logout(request))
