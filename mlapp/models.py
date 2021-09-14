from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Books(models.Model):
    ml_title = models.CharField(max_length=100)
    short_summary = models.TextField() 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Feature(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    ml_img = models.ImageField(default='images/0.jpg', upload_to='model_cover_pic')
    lnk = models.CharField(max_length=20, default="\{% url 'login' %\}")