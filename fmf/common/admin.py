from django.contrib import admin
from adminsortable.admin import SortableAdmin
from .models import Author, ExternalLink


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contribution', 'active')
    list_filter = ['active']
    search_fields = ['name']


class ExternalLinkAdmin(SortableAdmin):
    list_display = ('title', 'url', 'order')
    search_fields = ['title']


admin.site.register(Author, AuthorAdmin)
admin.site.register(ExternalLink, ExternalLinkAdmin)
