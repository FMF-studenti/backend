from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'date')
    list_filter = ['date']
    search_fields = ['author', 'content']

admin.site.register(Quote, QuoteAdmin)
