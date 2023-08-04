from django.http import HttpResponse
from django.shortcuts import render


# hello world page for testing
def hello_world(request):
    return HttpResponse("Hello world from django!")


# test base template

def base(request):
    return render(request, 'base.html', {})

# index page
def index(request):
    return render(request, 'index.html', {})
