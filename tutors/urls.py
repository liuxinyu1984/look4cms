from django.urls import path
from .views import TutorCourseList, TutorCourseDetail, TutorLectureDetail, TutorCreateLecture, TutorUpdateLecture, TutorDeleteLecture
from .views import tutor_course_list, tutor_course_detail, tutor_lecture_detail


urlpatterns = [
    path('tutor_course_list', tutor_course_list, name='tutor_course_list'),
    path('tutor_course_detail/<int:course_id>', tutor_course_detail, name='tutor_course_detail'),
    path('tutor_lecture_detail/<int:lecture_id>', tutor_lecture_detail, name='tutor_lecture_detail'),
    path('tutor_course_detail/<int:course_id>/tutor_create_lecture', TutorCreateLecture.as_view(), name='tutor_create_lecture'),
    path('tutor_lecture_detail/<int:lecture_id>/tutor_update_lecture', TutorUpdateLecture.as_view(), name='tutor_update_lecture'),
    path('tutor_lecture_detail/<int:lecture_id>/tutor_delete_lecture', TutorDeleteLecture.as_view(), name='tutor_delete_lecture'),
]
