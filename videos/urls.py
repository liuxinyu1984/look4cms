from django.urls import path
from .views import display_single_video, upload_video
from .views import tutor_video_detail, tutor_create_video, tutor_delete_video, tutor_update_video

urlpatterns = [
    path('', display_single_video), 
    path('upload', upload_video),
    path('tutor_video_detail/<int:video_id>', tutor_video_detail, name='tutor_video_detail'),
    path('tutor_create_video/<int:lecture_id>', tutor_create_video, name='tutor_create_video'),
    path('tutor_delete_video/<int:video_id>', tutor_delete_video, name='tutor_delete_video'),
    #path('tutor_update_video/<int:video_id>', tutor_update_video, name='tutor_update_video'),
]
