from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contribution', 'active')
    list_filter = ['active']
    search_fields = ['name']

admin.site.register(Author, AuthorAdmin)
