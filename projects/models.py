from django.db import models
from django.conf import settings


class Project(models.Model):

    title = models.Charfield(max_lenght=200)
    description = TextField(blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)