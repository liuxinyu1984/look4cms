from django.shortcuts import render
from .models import VimeoVideo
import vimeo, requests, json
from .vimeo_key import *

def display_single_video(request):

    video = VimeoVideo.objects.get(pk=2)

    client = vimeo.VimeoClient(
        token=personal_access_token,
        key=client_identifier,
        secret=client_secret
    )

    uri = 'https://api.vimeo.com/videos/' + video.video_id

    response = client.get(uri)
    response_json = response.json()

    uri = response_json["uri"]
    name = response_json["name"]
    link = response_json["link"]
    duration = response_json["duration"]
    html = response_json['embed']["html"]

    x_ratelimit_limit = response.headers['x-ratelimit-limit']
    x_ratelimit_remaining = response.headers['x-ratelimit-remaining']

    template = 'videos/display_single_video.html'

    context = {
        'video_id': video.video_id,
        'uri': uri,
        'name': name,
        'link': link,
        'duration': duration,
        'x_ratelimit_limit': x_ratelimit_limit,
        'x_ratelimit_remaining': x_ratelimit_remaining,
        'html': html
    }

    return render(request, template, context)