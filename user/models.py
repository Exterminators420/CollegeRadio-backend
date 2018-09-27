from django.db import models
from django.contrib.auth.models import User

import datetime
import os

def UploadTo(instance, filename):
    """
    Function for changing the upload image name
    """
    upload_to = '/Desktop/photos/users'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class User(models.Model):
    """
    This model extends all the basic information about an existing user
    """
 
    user = models.OneToOneField(
        to=User, 
        on_delete=models.CASCADE
    )
    

    last_active = models.DateField()
    
    picture = models.ImageField(
        upload_to=UploadTo , 
        blank=True,
        null=True,
    )
    likes = models.IntegerField(default=0)


      