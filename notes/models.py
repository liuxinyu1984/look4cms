from django.db import models
from courses.models import Lecture

def get_upload_to(instance, file_name):
    return 'notes/%s/%s' % (instance.lecture.course, file_name)


class Notes(models.Model):
    lecture = models.ForeignKey(
        Lecture,
        verbose_name='Lecture',
        on_delete=models.CASCADE,
        help_text='Lecture corresponds to this notes'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Title of notes',
        help_text='e.g. Week 1 notes'
    )
    upload_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Upload time'
    )
    document = models.FileField(
        upload_to=get_upload_to,
        verbose_name='Document to be uploaded'
    )

    def __str__(self):
        return self.title
