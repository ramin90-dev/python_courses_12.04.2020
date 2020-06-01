from django import forms

from teachers.models import Teachers


class TeachersCreateForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ('tech_name',
                  'tech_surn',
                  'tech_gend',
                  'tech_city',
                  'tech_age',
                  'tech_date',
                  'tech_phone',
                  )

    def clean_phone(self):
        phone = self.cleaned_data['tech_phone']
        cleaned_phone = ''.join(i for i in phone if i.isdigit())
        return cleaned_phone


class ContactUsForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    email_from = forms.EmailField(label='Your email', max_length=75)
    message = forms.CharField(label='Message', max_length=1024)
