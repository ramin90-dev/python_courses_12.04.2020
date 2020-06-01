from django import forms

from teachers.models import Teacher


class TeacherCreateForm (forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'age',
            'active_groups',
            'password',
            'phone'
        )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        clened_phone = ''
        for i in phone:
            if not i.isdigit():
                raise forms.ValidationError('enter numbers only')

        return clened_phone


class ContactUsForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    email_from = forms.EmailField(label='Your email', max_length=75)
    message = forms.CharField(label='Message', max_length=1024)
