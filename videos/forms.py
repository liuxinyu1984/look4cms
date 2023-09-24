from django import forms
from .models import VimeoVideo

class CreateVimeoVideoForm(forms.ModelForm):
    

    class Meta:
        model = VimeoVideo
        fields = ['title', 'uploader', 'lecture','uri']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
        }

    def __init__(self, *args, **kwargs):
        super(CreateVimeoVideoForm, self).__init__(*args, **kwargs)
        self.fields['uploader'].disabled = True
        self.fields['lecture'].disabled = True
        self.fields['uri'].disabled = True


class VideoFilePathForm(forms.Form):
    file_path = forms.CharField(
        help_text='Path of the video file (.mp4) on your computer.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    title = forms.CharField(
        help_text='Title of the video.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class VideoUploadForm(forms.Form):
    video_file = forms.FileField(
        help_text='Video file on your computer',
        widget=forms.FileInput
    )
    title = forms.CharField(
        help_text='Title of the video.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )