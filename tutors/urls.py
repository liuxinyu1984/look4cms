from django.urls import path
from .views import TutorCourseList



urlpatterns = [
    path('tutor_course_list', TutorCourseList.as_view(), name='tutor_course_list'),
]
