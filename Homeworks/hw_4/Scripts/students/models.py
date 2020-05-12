from django.db import models # noqa imported unused


class Students(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.age}'

    def info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'
