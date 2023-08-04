from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('', views.user_home, name='user_home'),
    path('user_profile', views.user_profile, name='user_profile'),
]
