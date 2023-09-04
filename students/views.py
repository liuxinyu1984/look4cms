from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from courses.models import Course, Lecture
from .models import Enrollment
from videos.models import VimeoVideo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateEnrollmentForm
from django.contrib.auth.decorators import login_required
import vimeo, requests, json
from videos.vimeo_key import *

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



###########################################
#### student course detail
###########################################

# CBV
class StudentCourseDetail(LoginRequiredMixin, DetailView):
    model = Enrollment
    template_name = 'students/student_course_detail.html'
    pk_url_kwarg = 'enrollment_id'

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)
    
# FBV
@login_required
def student_course_detail(request, enrollment_id):

    template = 'students/student_course_detail.html'
    enrollment = Enrollment.objects.get(pk=enrollment_id)

    if request.user != enrollment.student:
        is_right_student = False
        message = "Warning: You are not permitted to view this page!"
    else:
        is_right_student = True
        message = f"Course detail page of {enrollment.course}"

    context = {
        "is_right_student": is_right_student,
        "message": message,
        "enrollment": enrollment
    }
    return render(request, template, context)


###########################################
#### student lecture detail
###########################################

# CBV
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
    

# FBV
@login_required
def student_lecture_detail(request, enrollment_id, lecture_id):

    template = 'students/student_lecture_detail.html'
    enrollment = Enrollment.objects.get(pk=enrollment_id)
    lecture = Lecture.objects.get(pk=lecture_id)

    if request.user != enrollment.student:
        is_right_student = False
        message = "Warning: You are not permitted to view this page!"
    else:
        is_right_student = True
        message = f"Lecture detail page of {lecture}"
        

    context = {
        "is_right_student": is_right_student,
        "message": message,
        "lecture": lecture,
        "enrollment_id": enrollment.id
    }
    return render(request, template, context)







class PublicLecture(LoginRequiredMixin, DetailView):
    model = Lecture
    template_name = 'students/public_lecture.html'
    pk_url_kwarg = 'lecture_id'

    def get_queryset(self):
        return Lecture.objects.filter(is_public=True)
    



@login_required
def student_video_detail(request,enrollment_id, video_id):

    template = 'students/student_video_detail.html'
    enrollment = Enrollment.objects.get(pk=enrollment_id)
    video = VimeoVideo.objects.get(pk=video_id)

    if request.user != enrollment.student:
        is_right_student = False
        message = "Warning: You are not permitted to view this page!"
    else:
        is_right_student = True
        message = f"Video page of {video}"

    client = vimeo.VimeoClient(
        token=personal_access_token,
        key=client_identifier,
        secret=client_secret
    )

    uri =  video.uri

    response = client.get(uri)
    response_json = response.json()
    context = {
        "is_right_student": is_right_student,
        "message": message,
        "lecture_id": video.lecture.id,
        "enrollment_id": enrollment.id,
        "player_embed_url": response_json["player_embed_url"]
    }
    return render(request, template, context)