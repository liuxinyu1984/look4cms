from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from courses.models import Course, Lecture
from django.views.generic import ListView



class TutorCourseList(ListView):
    model = Course
    template_name = 'tutors/tutor_course_list.html'
    ordering = ['term', 'course_number']
    
    def get_queryset(self):
        return Course.objects.filter(tutor=self.request.user)