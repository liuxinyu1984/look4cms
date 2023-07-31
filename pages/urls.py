from django.urls import path
from . import views

urlpatterns = [
    path('hello_world', views.hello_world, name='hello_world'),
    path('', views.index, name='index')
]
