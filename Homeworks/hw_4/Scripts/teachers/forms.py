from django import forms

from teachers.models import teachers


class TeachersCreateForm(forms.ModelForm):
    class Meta:
        model = teachers
        fields = ('tech_name', 'tech_surn', 'tech_gend', 'tech_city', 'tech_age', 'tech_date')
