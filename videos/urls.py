from django.urls import path
from .views import display_single_video, upload_video

urlpatterns = [
    path('', display_single_video), 
    path('upload', upload_video),
]
