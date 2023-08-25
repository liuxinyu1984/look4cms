from django import forms
from django.forms import ModelForm
from courses.models import Lecture

class CreateLectureForm(ModelForm):
    
    class Meta:
        model = Lecture
        fields = '__all__'
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'week': forms.NumberInput(attrs={'class': 'form-control'}),
            'syllabus': forms.Textarea(attrs={'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_midterm': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_final': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateLectureForm, self).__init__(*args, **kwargs)
        self.fields['course'].disabled = True