from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from courses.models import Course, Lecture
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CreateLectureForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test



#############################################
# define the tutor_required decorator
user_login_required = user_passes_test(lambda user: user.is_tutor, login_url='/')

def tutor_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func


#################################################
# tutor course list view
#################################################

# CBV
class TutorCourseList(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'tutors/tutor_course_list.html'
    ordering = ['term', 'course_number']
    
    def get_queryset(self):
        #print(self.request.__dict__)
        #print(self.request.GET)
        return Course.objects.filter(tutor=self.request.user)

# FBV
@login_required
def tutor_course_list(request):
    template = 'tutors/tutor_course_list.html'
    if request.user.is_tutor == False:
        message = 'Warning: You Are Not a Tutor!'
        context = {
            "message": message
        }
    else:
        courses = Course.objects.filter(tutor=request.user).order_by('term', 'course_number')
        if not courses:
            message = "You currently have no course on teaching."
        else:
            message = f"All courses taught by {request.user}"

        context = {
            "message": message,
            "courses": courses
        }
    return render(request, template, context)
    
    
    
#################################################
# tutor course detail view
#################################################

# CBV
class TutorCourseDetail(LoginRequiredMixin, DetailView):
    model = Course
    pk_url_kwarg = 'course_id'
    template_name = 'tutors/tutor_course_detail.html'

    def get_queryset(self):
        return Course.objects.filter(tutor=self.request.user)
    
# FBV
@login_required
def tutor_course_detail(request, course_id):
    template = 'tutors/tutor_course_detail.html'
    course = Course.objects.get(pk=course_id)
    is_instructor = False

    if not request.user.is_tutor:
        message = 'Warning: You Are Not A Tutor!'
    elif course.tutor != request.user:
        message = "Warning: You are NOT the instructor of this course!"
    else:
        is_instructor = True
        message = f"Course homepage of {course} for instructor {request.user}"

    context = {
        "is_instructor": is_instructor,
        "message": message,
        "course": course
    }
    return render(request, template, context)
    
        
#################################################
# tutor lecture detail view
#################################################

# CBV
class TutorLectureDetail(LoginRequiredMixin, DetailView):
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


# FBV
@tutor_required
def tutor_lecture_detail(request, lecture_id):

    template = 'tutors/tutor_lecture_detail.html'
    lecture = Lecture.objects.get(pk=lecture_id)
    
    if request.user != lecture.course.tutor:
        is_instructor = False
        message = "Warning: You are not the instructor of this course!"
    else:
        is_instructor = True
        message = f"Lecture Detail Page of {lecture}"

    context = {
        "message": message,
        "is_instructor": is_instructor,
        "lecture": lecture
    }
    return render(request, template, context)



#################################################
# tutor lecture create view
#################################################

# CBV
class TutorCreateLecture(LoginRequiredMixin, CreateView):
    model = Lecture
    template_name = 'tutors/tutor_create_lecture.html'
    form_class = CreateLectureForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Course.objects.get(pk=self.kwargs['course_id'])
        context['course'] = course
        user_is_instructor = (course.tutor == self.request.user)
        context['user_is_instructor'] = user_is_instructor
        return context

    def get_initial(self):
        return {'course': Course.objects.get(id=self.kwargs['course_id'])}
    

# FBV
@tutor_required
def tutor_create_lecture(request, course_id):

    course = Course.objects.get(pk=course_id)
    template = 'tutors/tutor_create_lecture.html'

    if course.tutor != request.user:
        is_instructor = False
        message = "Warning: You are NOT instructor of this course!"
        return render(request, template, {"is_instructor": is_instructor, "message": message})
    else:
        is_instructor = True
        message = f"Create a new lecture for the course {course}"
        form = CreateLectureForm(request.POST or None, initial={"course": course})

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect ('tutor_course_detail', course.pk)

        context = {
            "course": course,
            "is_instructor": is_instructor,
            "message": message,
            "form": form
        }
        return render(request, template, context)









class TutorUpdateLecture(LoginRequiredMixin, UpdateView):
    model = Lecture
    template_name = 'tutors/tutor_update_lecture.html'
    pk_url_kwarg = 'lecture_id'
    fields = ['title', 'week', 'syllabus', 'is_public', 'is_midterm', 'is_final']

    def get_queryset(self):
        lecture = Lecture.objects.get(pk=self.kwargs['lecture_id'])
        if lecture.course.tutor == self.request.user:
            return Lecture.objects.filter(pk=self.kwargs['lecture_id'])
        else:
            return Lecture.objects.none()


class TutorDeleteLecture(LoginRequiredMixin, DeleteView):
    model = Lecture
    template_name = 'tutors/tutor_delete_lecture.html'
    pk_url_kwarg = 'lecture_id'

    def get_queryset(self):
        lecture = Lecture.objects.get(pk=self.kwargs['lecture_id'])
        if lecture.course.tutor == self.request.user:
            return Lecture.objects.filter(pk=self.kwargs['lecture_id'])
        else:
            return Lecture.objects.none()

    def get_success_url(self):
        return reverse_lazy('tutor_course_detail', kwargs={
            'course_id': self.object.course.id})