from django.contrib import admin
from .models import Enrollments

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'activated', 'dropped')

    list_filter = ('course', 'activated', 'dropped')
    search_fields = ['course', 'student__wechat_id']
    ordering = ['course', 'created_at']

admin.site.register(Enrollments, EnrollmentAdmin)