from django import forms

from group.models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_empl', 'group_name', 'title', 'info', 'group_phone')

    def clean_phone_group(self):
        pass
