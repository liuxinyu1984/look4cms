from django.db import models
from users.models import MyUser
from courses.models import Lecture
from backend.settings import MAX_WATCH

class VimeoVideo(models.Model):
    uri = models.CharField(
        max_length=200,
        verbose_name='Video URI',
        help_text='"/videos/xxxxxxxxx" from address bar of video',
        null=True,
    )
    uploader = models.ForeignKey(
        MyUser,
        verbose_name='Uploader',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    lecture = models.ForeignKey(
        Lecture,
        verbose_name='Lecture',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Title of Video',
        help_text='e.g. Week 1 Video'
    )
    upload_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Upload Time'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Update Time'
    )
    max_num_watch = models.PositiveIntegerField(
        default=MAX_WATCH,
        verbose_name='Watching Limit',
        help_text='Max number of times that a student can watch this video'
    )

    def __str__(self):
        return self.title
