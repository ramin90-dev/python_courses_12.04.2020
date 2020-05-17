from django.contrib import admin # noqa imported unused

from teachers.models import teachers


class TeachersAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('tech_name',
                    'tech_surn',
                    'tech_gend',
                    'tech_city',
                    'tech_age',
                    'tech_date'
                    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(age__gte=30)

        return queryset


admin.site.register(teachers, TeachersAdmin)
