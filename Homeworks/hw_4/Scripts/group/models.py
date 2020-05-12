from django.db import models # noqa imported unused


class Group(models.Model):
    group_empl = models.CharField(max_length=32)
    group_name = models.CharField(max_length=32)
    title = models.BooleanField()
    info = models.CharField(max_length=255)
