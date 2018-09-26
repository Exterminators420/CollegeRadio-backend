from django.db import models
import datetime
import os


class AbstractChannels(models.Model):
    """
    This model contains all the basic information neded for creating a channel
    """

    Channel_name = models.CharField(
        max_length=63,
        unique=True,
    )

    Channel_description = models.TextField(
        blank=True,
    )

    date_created = models.DateField(
        default=datetime.date.today,
    )

    likes = models.IntegerField(default=0)
    
    picture = models.ImageField(
        upload_to=UploadTo(),   #tbd
        blank=True,
        null=True,
    )


    class Meta:
        abstract = True

    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        name = self.Channel_name
        return f'{name} '

class UserChannel(AbstractChannels):
    user = models.ForeignKey(User, unique=True)

class CommonChannel(AbstractChannels):




