from typing import Any, Dict
from django.db import models
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


class StudentCourseList(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = 'students/student_course_list.html'

    def get_queryset(self, **kwargs):
        return Enrollment.objects.filter(student=self.request.user)


class StudentCourseDetail(LoginRequiredMixin, DetailView):
    model = Enrollment
    template_name = 'students/student_course_detail.html'
    pk_url_kwarg = 'enrollment_id'

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)
    

class StudentLectureDetail(LoginRequiredMixin, DetailView):
    model = Enrollment
    template_name = 'students/student_lecture_detail.html'
    pk_url_kwarg = 'enrollment_id'

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.activated:
            context['lecture'] = Lecture.objects.get(pk=self.kwargs['lecture_id'])
        return context