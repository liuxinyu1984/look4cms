from django.forms import ModelForm
from students.models import Enrollment

class CreateEnrollmentForm(ModelForm):
    
    class Meta:
        model = Enrollment
        fields = ('course', 'student')

    def __init__(self, *args, **kwargs):
        super(CreateEnrollmentForm, self).__init__(*args, **kwargs)
        self.fields['course'].disabled = True
        self.fields['student'].disabled = True