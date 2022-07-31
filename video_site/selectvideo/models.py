from django.contrib.auth.models import User
from django.db import models


class Attributes(models.Model):
    attribute_name = models.CharField(max_length=256, blank=False, null=False)


class Title(models.Model):
    title_name = models.CharField(max_length=256, blank=False, null=False)
    tags = models.ManyToManyField(
        Attributes,
        related_name='+'
    )
    desc = models.TextField('description')


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
