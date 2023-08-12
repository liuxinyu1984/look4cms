from django.forms import ModelForm
from courses.models import Lecture

class CreateLectureForm(ModelForm):
    
    class Meta:
        model = Lecture
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateLectureForm, self).__init__(*args, **kwargs)
        self.fields['course'].disabled = True