from django.urls import path
from .views import AllCourseList, CourseIntroduction, RegisterCourse, StudentCourseList, StudentCourseDetail, StudentLectureDetail, PublicLecture
from .views import student_course_detail, student_lecture_detail, student_video_detail

urlpatterns = [
    path('all_course_list', AllCourseList.as_view(), name='all_course_list'),
    path('course_introduction/<int:pk>', CourseIntroduction.as_view(), name='course_introduction'),
    path('register_course/<int:pk>', RegisterCourse.as_view(), name='register_course'),
    path('student_course_list', StudentCourseList.as_view(), name='student_course_list'),
    path('student_course_detail/<int:enrollment_id>', student_course_detail, name='student_course_detail'),
    path('student_course_detail/<int:enrollment_id>/lecture/<int:lecture_id>', student_lecture_detail, name='student_lecture_detail'),
    path('public_lecture/<int:lecture_id>', PublicLecture.as_view(), name='public_lecture'),
    path('student_course_detail/<int:enrollment_id>/video/<int:video_id>', student_video_detail, name='student_video_detail'),
    
]

# test MAX_WATCH value
# urlpatterns += [
#     path('test_max_watch', test_max_watch)
# ]
