from django.db import models

class group(models.Model):
    group_empl = models.CharField(max_length=32)# Имя участника
    group_name = models.CharField(max_length=32)# Имя группы
    title = models.BooleanField()#
    info = models.CharField(max_length=255) #доп инфо




