from django.db import models


class teachers(models.Model):
    tech_name = models.CharField(max_length=32)  # Имя
    tech_surn = models.CharField(max_length=32)  # отчество
    tech_gend = models.BooleanField()  # пол учителя ( Поле хранящее значение true/false.)
    tech_city = models.CharField(max_length=64)  # город работы
    tech_age = models.PositiveIntegerField()  # возраст
    tech_date = models.DateField()  # дата прийома(запись текущей датой) https://djbook.ru/rel1.9/ref/models/fields.html#booleanfield


    @property
    def full_info(self):
        return f'{self.tech_name} {self.tech_surn} {self.tech_gend} {self.tech_city} {self.tech_date}'


    def name_gend(self):
        return f'{self.tech_name} {self.tech_surn} {self.tech_gend}'


    def info_date(self):
    return f'{self.tech_name} {self.tech_surn} {self.tech_age} {self.tech_date}'