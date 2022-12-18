from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
#afmin - afripal admin 

class User(AbstractUser):
        profile_pic = CloudinaryField('image')
        is_afmin = models.BooleanField(default=False)