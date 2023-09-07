from django import forms
from .models import Notes


class CreateNoteForm(forms.Form):
    title = forms.CharField(
        help_text='Title of notes, e.g. Week1 Notes',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    document = forms.FileField(
        help_text='PDF file to upload',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )