from typing import Any, Dict
from django.shortcuts import render
from courses.models import Course, Lecture
from .models import Enrollment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateEnrollmentForm

class AllCourseList(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/all_course_list.html'


class CourseIntroduction(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course_introduction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs['pk'])
        return context

class RegisterCourse(LoginRequiredMixin, CreateView):
    model = Enrollment
    template_name = 'students/register_course.html'
    form_class = CreateEnrollmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs['pk'])
        return context

    def get_initial(self):
        course = Course.objects.get(pk=self.kwargs['pk'])
        student = self.request.user
        return {'course': course, 'student': student }
    