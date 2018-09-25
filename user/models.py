from django.db import models
import datetime
import os

class User(Model):
    """
    This model contains all the basic information about an existing user
    """

    username = models.CharField(
        max_length=63,
        unique=True,
    )

    email = models.EmailField(
      unique = True,
    )

    name = models.CharField(
        max_length=63,
    )

    date = models.DateField(
        default=datetime.date.today,
    )

    last_active = models.DateField()
    
    picture = models.ImageField(
        upload_to=UploadTo(),
        blank=True,
        null=True,
    )

    likes = models.IntegerField()


    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        username = self.username
        return f'{username}}'