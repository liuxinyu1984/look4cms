from django.shortcuts import render
from courses.models import Course, Lecture
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AllCourseList(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/all_course_list.html'


class CourseIntroduction(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course_introduction.html'