from django.urls import path
from .views import AllCourseList, CourseIntroduction, RegisterCourse

urlpatterns = [
    path('all_course_list', AllCourseList.as_view(), name='all_course_list'),
    path('course_introduction/<int:pk>', CourseIntroduction.as_view(), name='course_introduction'),
    path('register_course/<int:pk>', RegisterCourse.as_view(), name='register_course'),
]
