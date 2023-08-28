from django.shortcuts import render
from .models import VimeoVideo
import vimeo, requests, json
from .vimeo_key import *
from users.models import MyUser
from courses.models import Lecture
from .forms import CreateVimeoVideoForm, VideoFilePathForm

def display_single_video(request):

    video = VimeoVideo.objects.get(pk=6)

    client = vimeo.VimeoClient(
        token=personal_access_token,
        key=client_identifier,
        secret=client_secret
    )

    uri =  video.uri

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
        'uri': uri,
        'name': name,
        'link': link,
        'duration': duration,
        'x_ratelimit_limit': x_ratelimit_limit,
        'x_ratelimit_remaining': x_ratelimit_remaining,
        'html': html
    }

    return render(request, template, context)


def upload_video(request):
    template = 'videos/create_single_video.html'
    # prepopulate the form
    uploader = MyUser.objects.get(pk=2)
    lecture = Lecture.objects.get(pk=1)

    video_form = VideoFilePathForm(request.POST or None)
    

    if request.method == "POST":
        if video_form.is_valid():
            client = vimeo.VimeoClient(
                token=personal_access_token,
                key=client_identifier,
                secret=client_secret
            )

            file_path = video_form['file_path'].value()
            name = video_form['title'].value()

            uri = client.upload(
                file_path,
                data = {
                    'name': name
                }
            )
            

            response = client.get(uri + '?fields=transcode.status').json()
            if response['transcode']['status'] == 'error':
                message = 'Upload Error! Try upload video again. Make sure your file path is correct.'
                return render(request, 'videos/upload_error.html', {"message": message})
            else:
                message = 'Upload Successful! Your video is being transcoded.'
                vimeo_video = VimeoVideo(
                    uri=uri,
                    uploader = uploader,
                    lecture = lecture,
                    title = name
                )
                vimeo_video.save()

                return render(request, 'videos/upload_success.html', {"message": message})
    
    context = {
        "form": video_form
    }
    return render(request, template, context)