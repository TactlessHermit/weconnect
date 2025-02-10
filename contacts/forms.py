from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=Contact.SEX_CHOICES
    )

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'gender', 'nationality', 'email', 'job', 'experience', 'birthday', 'bio']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }