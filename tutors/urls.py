from django.urls import path
from .views import TutorCourseList, TutorCourseDetail, TutorLectureDetail



urlpatterns = [
    path('tutor_course_list', TutorCourseList.as_view(), name='tutor_course_list'),
    path('tutor_course_detail/<int:course_id>', TutorCourseDetail.as_view(), name='tutor_course_detail'),
    path('tutor_lecture_detail/<int:lecture_id>', TutorLectureDetail.as_view(), name='tutor_lecture_detail'),
]
