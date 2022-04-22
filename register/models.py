from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'




def creat_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])



post_save.connect(creat_profile,sender=User)
