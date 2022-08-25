from django.contrib.auth.models import User
from django.db import models
from pathlib import Path

thumbnail_path = Path('/home/app_user/server/media/thumbnails')


class Attributes(models.Model):
    attribute_name = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.attribute_name


class Title(models.Model):
    title_name = models.CharField(max_length=256, blank=False, null=False)
    tags = models.ManyToManyField(
        Attributes,
        related_name='+'
    )
    desc = models.TextField(
        'description', default='No description is available for this title')
    tumbnail = models.ImageField(
        upload_to='thumbnails/', default=thumbnail_path)
    date_added = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    viewed_titles = models.ManyToManyField(
        Title,
        related_name='+'
    )
    last_login = models.DateTimeField()
    watchlist = models.ManyToManyField(
        Title,
        related_name='+'
    )
