from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=255)
    auther = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
   
