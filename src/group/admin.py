from django.contrib import admin  # noqa -file not used
from django.contrib import admin

from group.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('id', 'first_name', 'last_name', 'group_code', 'group_number',
                    'form_of_training', 'training_completed', 'head', 'curator')
    fields = ('first_name', 'last_name', 'group_code', 'group_number', 'form_of_training', 'training_completed',
              'head', 'curator')
    readonly_fields = ('form_of_training', 'training_completed')
    select_related = ['head', 'curator']


admin.site.register(Group, GroupAdmin) # noqa
