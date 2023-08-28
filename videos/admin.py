from django.contrib import admin
from .models import VimeoVideo

class VimeoVideoAdmin(admin.ModelAdmin):
    list_display = ('uri', 'id', 'uploader', 'lecture', 'title', 'upload_at')
    ordering = ['uploader', 'lecture']
    list_filter = ('uploader', 'lecture')
    search_fields = ['uploader','lecture']
    readonly_fields = ('id', 'upload_at')

    fieldsets = (
        ('Video Info', {'fields':('uri', 'id', 'title', 'upload_at')}),
        ('Uploader Info', {'fields':('uploader',)}),
        ('Lecture', {'fields':('lecture',)})
    )

admin.site.register(VimeoVideo, VimeoVideoAdmin)