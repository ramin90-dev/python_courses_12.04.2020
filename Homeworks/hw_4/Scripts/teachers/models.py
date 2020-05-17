from django.db import models # noqa imported unused


class teachers(models.Model):
    tech_name = models.CharField(max_length=32)
    tech_surn = models.CharField(max_length=32)
    tech_gend = models.BooleanField()
    tech_city = models.CharField(max_length=64)
    tech_age = models.PositiveIntegerField()
    tech_date = models.DateField()

    @property
    def fu(self):
        return f'{self.tech_name} {self.tech_surn} {self.tech_gend}'

    def full_info(self):
        return f'{self.id} {self.tech_name} {self.tech_surn} {self.tech_gend} {self.tech_city} ' \
               f'{self.tech_age} {self.tech_date}'

    def info_date(self):
        return f'{self.tech_name} {self.tech_surn} {self.tech_age} {self.tech_date}'
