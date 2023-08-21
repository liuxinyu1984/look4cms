from django.shortcuts import render
from .models import EmbedVideo


def test(request):
    videos = EmbedVideo.objects.all()
    context = {
        'videos': videos
    }
    template = 'embeds/test.html'
    return render(request, template, context)
