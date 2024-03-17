from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import forms
from django.forms.widgets import PasswordInput
from django.utils.safestring import mark_safe


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, verbose_name="")
    address = models.CharField(max_length=200, verbose_name="")
    city = models.CharField(max_length=20, verbose_name="")
    country = models.CharField(max_length=20, verbose_name="")
    image = models.ImageField(upload_to='images/users/', default='images/users/default.jpg', verbose_name="")

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}"/>')

    def __str__(self):
        return self.username

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)