from django import forms

from group.models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'first_name',
            'last_name',
            'group_code',
            'group_number',
            'training_completed',
            'form_of_training',
            'head',
            'curator'
        )
