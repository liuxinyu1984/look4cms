from django.urls import path
from .views import display_single_video, upload_video
from .views import tutor_video_detail

urlpatterns = [
    path('', display_single_video), 
    path('upload', upload_video),
    path('tutor_video_detail/<int:video_id>', tutor_video_detail, name='tutor_video_detail'),
]
