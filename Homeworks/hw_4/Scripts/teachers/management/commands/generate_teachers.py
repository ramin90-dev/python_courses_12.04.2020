import random

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import teachers


class Command(BaseCommand):
    help = 'Generates new teachers (default = 100)' # noqa is a python builtin

    def add_arguments(self, parser):
        parser.add_argument('value', nargs='?', type=int, help='Value teachers', default=100)

    def handle(self, *args, **kwargs):
        value = kwargs['value']
        fake = Faker()
        teachers_gend = ['True', 'False']
        random_age = random.randint(20, 60)
        datetime = ['2020-02-20']

        ap_teachers = []
        for _ in range(value):
            ap_teachers.append(teachers(
                tech_name=fake.first_name(),
                tech_surn=fake.last_name(),
                tech_gend=random.choice(teachers_gend),  # Мужской/Женский
                tech_city=fake.first_name(),  # подставил Имя вместо города
                tech_age=random_age,
                tech_date=random.choice(datetime),
            ))

        teachers.objects.bulk_create(ap_teachers)
