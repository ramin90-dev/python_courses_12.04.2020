from django.db import models # noqa imported unused


class Teachers(models.Model):
    tech_name = models.CharField(max_length=32)
    tech_surn = models.CharField(max_length=32)
    tech_gend = models.BooleanField()
    tech_city = models.CharField(max_length=64)
    tech_age = models.PositiveIntegerField()
    tech_date = models.DateField()
    tech_phone = models.CharField(max_length=24, default='')

    @property
    def fu(self):
        return f'{self.tech_name} {self.tech_surn} {self.tech_gend} {self.tech_phone}'

    def full_info(self):
        return f'{self.id} {self.tech_name} {self.tech_surn} {self.tech_gend} {self.tech_city} {self.tech_phone}' \
               f'{self.tech_age} {self.tech_date}'

    def info_date(self):
        return f'{self.tech_name} {self.tech_surn} {self.tech_age} {self.tech_date}'


class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=64)
    execution_time = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
