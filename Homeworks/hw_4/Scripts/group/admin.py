from django.contrib import admin # noqa imported unused

from group.models import Group


class GroupsAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('group_empl',
                    'group_name',
                    'title',
                    'info'
                    )


admin.site.register(Group, GroupsAdmin)
