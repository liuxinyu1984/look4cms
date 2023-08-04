from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views import View
from .models import MyUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.forms.models import model_to_dict


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

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = MyUser
    fields = ('username', 'email', 'wechat_id')
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('user_profile')

    def get_object(self):
        return self.request.user

# @login_required
# def edit_user_profile(request, user_id):
#     user = get_object_or_404(MyUser, pk=user_id)
#     if request.method == "GET":
#         form = EditProfileForm(initial=model_to_dict(user))
#         return render(request, 'registration/edit_profile.html', {'form':form})
#     elif request.method == "POST":
#         form = EditProfileForm(request.POST, instance=user)
#         if form.is_valid():
#              form.save()
#              return HttpResponseRedirect(reverse_lazy('user_profile'))
#         else:
#              return HttpResponse('Form not valid')