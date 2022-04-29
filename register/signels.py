from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import  Profile
from  django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


@receiver(post_save,sender=User)
def save_profile(sender,**kwargs):
    kwargs['instance'].profile.save()