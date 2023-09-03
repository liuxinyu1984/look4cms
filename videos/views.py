from django.shortcuts import render, redirect
from .models import VimeoVideo
import vimeo, requests, json
from .vimeo_key import *
from users.models import MyUser
from courses.models import Lecture
from .forms import CreateVimeoVideoForm, VideoFilePathForm
from tutors.views import tutor_required

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





#######################################################################################
#########    views
#######################################################################################

#############################  display video
@tutor_required
def tutor_video_detail(request, video_id):

    template = 'videos/tutor_video_detail.html'
    is_instructor = False
    video = VimeoVideo.objects.get(pk=video_id)

    if request.user != video.lecture.course.tutor:
        message = 'You cannot watch this video. (Not the tutor of this course)'
    else:
        is_instructor = True
        message = f'Detail of video: {video}'

    # fetch video uri from Vimeo
    client = vimeo.VimeoClient(
        token=personal_access_token,
        key=client_identifier,
        secret=client_secret
    )

    uri =  video.uri

    response = client.get(uri)
    response_json = response.json()

    # uri = response_json["uri"]
    # name = response_json["name"]
    # link = response_json["link"]
    html = response_json['embed']["html"]

    context = {
        "video": video,
        "is_instructor": is_instructor,
        "message": message,
        "uri": uri,
        "html": html,
        "player_embed_url": response_json["player_embed_url"]
    }

    return render(request, template, context)

#######################################  upload video for a lecture
@tutor_required
def tutor_create_video(request, lecture_id):

    template = 'videos/tutor_create_video.html'
    lecture = Lecture.objects.get(pk=lecture_id)
    uploader = request.user

    if request.user != lecture.course.tutor:
        message = "Warning: You cannot upload video to this lecture! (Not the instructor)"
        is_instructor = False
    else:
        message = f"Upload video to {lecture}"
        is_instructor = True

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
        "form": video_form,
        "message": message,
        "is_instructor": is_instructor,
        "lecture": lecture
    }
    return render(request, template, context)


###############################################  delete an existing video
@tutor_required
def tutor_delete_video(request, video_id):

    template = 'videos/tutor_delete_video.html'
    video = VimeoVideo.objects.get(pk=video_id)
    lecture_id = video.lecture.id

    if request.user != video.lecture.course.tutor:
        is_instructor = False
        message = 'You cannot delete this video. (Not the tutor of this course)'
        context = {
            "is_instructor": is_instructor,
            "message": message
        }
        return render(request, template, context)
    else:
        is_instructor = True
        message = f'Delete video: {video}'

        if request.method == "POST":
            client = vimeo.VimeoClient(
              token=personal_access_token,
              key=client_identifier,
              secret=client_secret
            )
            uri = video.uri
            client.delete(uri)
            video.delete()
            return redirect('tutor_lecture_detail', lecture_id)

        context = {
            "is_instructor": is_instructor,
            "message": message,
            "lecture_id": lecture_id,
            "video_id": video.id
        }
        return render(request, template, context)
    

#################################################### update an existing video
@tutor_required
def tutor_update_video(request, video_id):

    template = 'videos/tutor_update_video.html'
    video = VimeoVideo.objects.get(pk=video_id)
    uri = video.uri

    if request.user != video.lecture.course.tutor:
        message = "Warning: You cannot update this video! (Not the instructor of this course)"
        is_instructor = False
    else:
        message = f"Update video {video}"
        is_instructor = True
    
    form = VideoFilePathForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            client = vimeo.VimeoClient(
                token=personal_access_token,
                key=client_identifier,
                secret=client_secret
            )

            file_path = form['file_path'].value()
            name = form['title'].value()

            new_uri = client.replace(
                video_uri=uri,
                filename=file_path,
                data = {
                    'name': name
                }
            )

            video.title = name

            return redirect('tutor_video_detail', video.id)


    context = {
        "is_instructor": is_instructor,
        "video": video,
        "form": form
    }
    return render(request, template, context)