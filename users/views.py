from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.urls import reverse_lazy

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



class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')