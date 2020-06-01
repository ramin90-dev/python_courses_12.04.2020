from django.db import models # noqa imported unused


class Group(models.Model):
    group_empl = models.CharField(max_length=32)
    group_name = models.CharField(max_length=32)
    title = models.BooleanField()
    info = models.CharField(max_length=255)
    group_phone = models.CharField(max_length=24, default='')

    @property
    def full_info(self):
        return f'{self.group_empl} {self.group_name} {self.title} {self.info} {self.group_phone}'

    def data(self):
        return f'{self.id} {self.group_empl} {self.group_name} {self.title} {self.info} {self.group_phone}'


class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=64)
    execution_time = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
