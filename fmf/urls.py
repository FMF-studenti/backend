"""fmf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework import routers
from oauth2_provider import views as oauth2_provider

from fmf.common import views as common_views
from fmf.discourse import views as discourse_views
from fmf.notes import views as notes_views
from fmf.quotes import views as quotes_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'authors', common_views.AuthorViewSet)
router.register(r'blogArticles', common_views.BlogArticleViewSet,
                base_name='blogArticles')
router.register(r'externalLinks', common_views.ExternalLinkViewSet)

router.register(r'notes/departments', notes_views.DepartmentViewSet)
router.register(r'notes/levels', notes_views.LevelViewSet)
router.register(r'notes/years', notes_views.YearViewSet)
router.register(r'notes/subjects', notes_views.SubjectViewSet)
router.register(r'notes/notes', notes_views.NoteViewSet)
router.register(r'notes/files', notes_views.FileViewSet, base_name='files')

router.register(r'quotes', quotes_views.QuoteViewSet, base_name='quotes')

router.register(r'topics', discourse_views.TopicViewSet, base_name='topics')
router.register(r'users', discourse_views.UserViewSet, base_name='users')

router.register(r'pm', discourse_views.PrivateMessageViewSet, base_name='pm')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/authorize/$', oauth2_provider.AuthorizationView.as_view()),
    url(r'^auth/token/$', oauth2_provider.TokenView.as_view()),
    url(r'^auth/revoke_token/$', oauth2_provider.RevokeTokenView.as_view()),
    url(r'^auth/finalise/', common_views.logout_view),
    url(r'^auth/forum_logout/', discourse_views.UserLogoutView.as_view()),

    url(r'^auth/$', RedirectView.as_view(url='/auth/login/', permanent=True)),
    url(r'^auth/login/$',
        RedirectView.as_view(url='/auth/login/discourse/', permanent=False)),
    url(r'^auth/', include('social.apps.django_app.urls', namespace='social'))
]

# Misc
admin.site.site_title = 'Študentske strani FMF'
admin.site.site_header = 'Študentske strani FMF - Admin'
