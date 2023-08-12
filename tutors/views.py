from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from courses.models import Course, Lecture
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CreateLectureForm



class TutorCourseList(ListView):
    model = Course
    template_name = 'tutors/tutor_course_list.html'
    ordering = ['term', 'course_number']
    
    def get_queryset(self):
        #print(self.request.__dict__)
        #print(self.request.GET)
        return Course.objects.filter(tutor=self.request.user)
    

class TutorCourseDetail(DetailView):
    model = Course
    pk_url_kwarg = 'course_id'
    template_name = 'tutors/tutor_course_detail.html'

    def get_queryset(self):
        return Course.objects.filter(tutor=self.request.user)
        

class TutorLectureDetail(DetailView):
    model = Lecture
    pk_url_kwarg = 'lecture_id'
    template_name = 'tutors/tutor_lecture_detail.html'

    def get_queryset(self):
        lecture = Lecture.objects.get(pk=self.kwargs['lecture_id'])
        if lecture.course.tutor == self.request.user:
            return Lecture.objects.filter(pk=self.kwargs['lecture_id'])
        else:
            return Lecture.objects.none()
        
# # This also works
# class TutorLectureDetail2(DetailView):
#     model = Lecture
#     pk_url_kwarg = 'lecture_id'
#     template_name = 'tutors/tutor_lecture_detail.html'

#     def get_queryset(self):
#         courses = Course.objects.filter(tutor=self.request.user)
#         return Lecture.objects.filter(course__in=courses)


class TutorCreateLecture(CreateView):
    model = Lecture
    template_name = 'tutors/tutor_create_lecture.html'
    form_class = CreateLectureForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Course.objects.get(pk=self.kwargs['course_id'])
        context['course'] = course
        return context

    def get_initial(self):
        return {'course': Course.objects.get(id=self.kwargs['course_id'])}
    


class TutorUpdateLecture(UpdateView):
    model = Lecture
    template_name = 'tutors/tutor_update_lecture.html'
    pk_url_kwarg = 'lecture_id'
    fields = ['title', 'week', 'syllabus', 'is_public', 'is_midterm', 'is_final']