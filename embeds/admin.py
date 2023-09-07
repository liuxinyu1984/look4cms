from django.contrib import admin
from .models import EmbedVideo
from embed_video.admin import AdminVideoMixin

class EmbedVideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('video', 'uploader', 'lecture', 'title', 'upload_at')
    ordering = ['uploader', 'lecture']
    list_filter = ('uploader', 'lecture')
    search_fields = ['uploader','lecture']


# admin.site.register(EmbedVideo, EmbedVideoAdmin)