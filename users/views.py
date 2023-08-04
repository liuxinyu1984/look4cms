from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required


@login_required
def user_home(request):
    contents = {
        'user': request.user
    }
    return render(request, 'user_home.html', contents)

@login_required
def user_profile(request):
    contents = {
        'user': request.user
    }
    return render(request, 'user_profile.html', contents)


# class UserHome(View):
#     def get(self, request):
#         content = {
#             'username': request.user.username
#         }
