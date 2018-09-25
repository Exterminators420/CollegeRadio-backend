from django.db import models
import datetime
import os


class Channels(Model):
    """
    This model contains all the basic information neded for reporting an item
    """

    user = models.ForeignKey(User, blank=True,)

    Channel_name = models.CharField(
        max_length=63,
    )

    Channel_description = models.TextField(
        blank=True,
    )

    date_created = models.DateField(
        default=datetime.date.today,
    )
    
    picture = models.ImageField(
        upload_to=UploadTo('lost_and_found', 'lost'),
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        name = self.name
        person = self.person

        return f'{name} - {person}'


class LostItem(AbstractItem):
    """
    This model implements AbstractItem for lost items
    """

    pass


class FoundItem(AbstractItem):
    """
    This model implements AbstractItem for found items
    """

    pass

