from django.contrib import admin
from .models import VimeoVideo

class VimeoVideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'uploader', 'lecture', 'title', 'upload_at')
    ordering = ['uploader', 'lecture']
    list_filter = ('uploader', 'lecture')
    search_fields = ['uploader','lecture']

admin.site.register(VimeoVideo, VimeoVideoAdmin)