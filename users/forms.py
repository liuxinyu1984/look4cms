from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

from .models import MyUser


class SignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'wechat_id')