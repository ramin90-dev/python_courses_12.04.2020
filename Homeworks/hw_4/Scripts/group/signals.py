from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Group


@receiver(pre_save, sender=Group)
def group_pre_save(sender, instance, **kwargs):
    instance.group_empl = instance.group_empl.capitalize()
    instance.group_name = instance.group_name.capitalize()
