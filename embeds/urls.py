from django.urls import path
from .views import test

urlpatterns = [
    path('test_embeds', test, name='test_embed_video'),
]
