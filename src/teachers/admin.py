from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'first_name', 'last_name', 'age', 'specification', 'active_groups')
    fields = ('first_name', 'last_name', 'age', 'specification', 'active_groups')
    readonly_fields = ('specification', 'active_groups')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(age__gt=18)

        return queryset

admin.site.register(Teacher, TeacherAdmin) # noqa
