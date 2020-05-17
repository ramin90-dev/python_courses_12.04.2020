from django.db import models # noqa imported unused


class Group(models.Model):
    group_empl = models.CharField(max_length=32)
    group_name = models.CharField(max_length=32)
    title = models.BooleanField()
    info = models.CharField(max_length=255)

    @property
    def full_info(self):
        return f'{self.group_empl} {self.group_name} {self.title} {self.info}'

    def data(self):
        return f'{self.id} {self.group_empl} {self.group_name} {self.title} {self.info}'
