from django.contrib import admin
from .models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'title', 'upload_at')


admin.site.register(Notes, NotesAdmin)