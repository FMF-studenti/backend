from django.contrib import admin
from .models import Department, Level, Year, Subject, Note


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'level', 'department')
    list_filter = ['department', 'level', 'year']
    search_fields = ['name', 'year', 'level', 'department']


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject')
    list_filter = ['time']
    search_fields = ['title', 'description', 'author', 'uploader']


admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Year)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Note, NoteAdmin)
