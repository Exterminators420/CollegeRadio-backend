from django.db import models
import datetime
import os


def UploadTo(instance, filename):
    """
    Function for changing the upload image name
    """
    upload_to = '/Desktop/photos'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)


class AbstractChannel(models.Model):
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

    likes = models.IntegerField(
        default=0
    )
    
    picture = models.ImageField(
        upload_to=UploadTo,
        blank=True,
        null=True,
    )


    class Meta:
        """
        Meta class for AbstractItem
        """

        abstract = True

    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        name = self.Channel_name
        return f'{name} '


class UserChannel(AbstractChannel):
    """
    The model which defines channels particulaar to a single user
    """
    user = models.ForeignKey(
        to=User, 
        unique=True,
        on_delete=models.CASCADE,
    )


class CommonChannel(AbstractChannel):
    """
    The model which defines common channels accessible to all channels.
    """
    pass




