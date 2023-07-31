from django.db import models
from django.contrib.auth.models import AbstractUser


# user model
class MyUser(AbstractUser):
    wechat_id = models.CharField(
        max_length=20,
        blank=False,
        unique=True,
        verbose_name='Wechat ID',
        help_text="Your Wechat/Weixin ID used to contact Look4Tutor service",
    )
    is_tutor = models.BooleanField(
        default=False, 
        verbose_name='Tutor',
        help_text="Designates whether the user is a tutor",
    )
    nickname = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Nickname',
        help_text="Nickname used by Look4Tutor",
    )
    label = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Label',
        help_text="Label added by administration"
    )
    comment = models.TextField(
        max_length=300,
        blank=True,
        verbose_name='Comment',
        help_text="Comment on user"
    )