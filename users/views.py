from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required


@login_required
def user_home(request):
    context = {
        'user': request.user
    }
    return render(request, 'user_home.html', context)

@login_required
def user_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'user_profile.html', context)



