from tkinter import N
from django.db import models


class Attributes(models.Model):
    attribute_name = models.CharField(max_length=256, blank=False, null=False)
    
class Title(models.Model):
    title_name = models.CharField(max_length=256, blank=False, null=False)
    tags = models.ManyToManyField(
        Attributes
    )