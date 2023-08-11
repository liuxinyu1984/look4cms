from django.contrib import admin
from .models import Term, Course, Lecture
from django.utils.timezone import datetime


class TermAdmin(admin.ModelAdmin):

    def term_title(self, obj):
        return obj.year + "-" + obj.season.lower()
    
    list_display = ('term_title', 'year', 'season', 'start_date', 'end_date')
    

admin.site.register(Term, TermAdmin)




class CourseAdmin(admin.ModelAdmin):

    def course_title(self, obj):
        return obj.subject + " " + obj.course_number

    def is_active(self, obj):
        return datetime.today().date() >= obj.term.start_date and datetime.today().date() <= obj.term.end_date

    list_display = ('course_title', 'term', 'section',
                    'tutor', 'is_active')
    # fields = ['subject', 'course_number', 'term', 'section', 'instructor', 'start_date', 'end_date']
    fieldsets = (
        ('Course', {'fields': ('subject', 'course_number', 'section')}),
        ('Time', {'fields': ('term',)}),
        ('Tutor', {'fields': ('tutor',)})
    )
    ordering = ['subject', 'course_number', 'tutor']
    list_filter = ('subject', 'tutor')
    search_fields = ['subject', 'tutor__username']


admin.site.register(Course, CourseAdmin)




class LectureAdmin(admin.ModelAdmin):

    # def course_title(self):
    #     return self.course.__str__()

    list_display = ('course', 'week', 'title' ,'is_public', 'is_midterm', 'is_final')
    # prepopulated_fields = {"slug": ['course', 'week']}
    list_filter = ('course',)
    search_fields = ['course']


admin.site.register(Lecture, LectureAdmin)
