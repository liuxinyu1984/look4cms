from django.db import models
from users.models import MyUser
from courses.models import Course
from django.urls import reverse

class Enrollment(models.Model):
    student = models.ForeignKey(
        MyUser,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='User (Student)'
    )
    course = models.ForeignKey(
        Course,
        models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Course'
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Registration Time'
    )
    activated = models.BooleanField(
        default=False,
        verbose_name='Activated by Administration'
    )
    dropped = models.BooleanField(
        default=False,
        verbose_name='Course Dropped by Student'
    )
    nums_watched = models.JSONField(
        default=dict,
        verbose_name='Times Watched',
        help_text='Dictionary of times of watching on each video'
    )

    def __str__(self):
        return str(self.course) + " by " + str(self.student)
    
    def get_absolute_url(self):
        return reverse("course_introduction", args=[int(self.course.id)])
    
