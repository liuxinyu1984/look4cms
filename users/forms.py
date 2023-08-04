from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin

from .models import MyUser


# form for user sign-up/create account
# username, email, wechat_id are required
class SignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'wechat_id')

# form for user to change profile
# a user can change username, email, wechat_id
# class EditProfileForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ('username', 'email', 'wechat_id')

        