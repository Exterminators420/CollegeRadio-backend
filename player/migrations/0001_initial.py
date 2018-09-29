<<<<<<< HEAD
# Generated by Django 2.1.1 on 2018-09-26 21:11
=======
# Generated by Django 2.1.1 on 2018-09-28 17:20
>>>>>>> da266dc032821ba4e71ab112c6755e3383f84cba

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import player.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Channel_name', models.CharField(max_length=63, unique=True)),
                ('Channel_description', models.TextField(blank=True)),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('likes', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=player.models.UploadTo)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Channel_name', models.CharField(max_length=63, unique=True)),
                ('Channel_description', models.TextField(blank=True)),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('likes', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=player.models.UploadTo)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
