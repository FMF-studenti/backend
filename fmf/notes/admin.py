from django.contrib import admin
from .models import Department, Level, Year, Subject, Note


class CommonNotesAdmin(admin.ModelAdmin):
    ordering = ('name',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'level', 'department')
    list_filter = ['department', 'level', 'year']
    search_fields = ['name', 'year', 'level', 'department']
    ordering = ('name', 'department', 'level', 'year')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject', 'time')
    list_filter = ['time']
    search_fields = ['title', 'description', 'author', 'uploader']


admin.site.register(Department, CommonNotesAdmin)
admin.site.register(Level, CommonNotesAdmin)
admin.site.register(Year, CommonNotesAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Note, NoteAdmin)
