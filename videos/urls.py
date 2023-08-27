from django.urls import path
from .views import display_single_video

urlpatterns = [
    path('', display_single_video)
]
