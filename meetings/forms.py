from django import forms
from .models import Meeting


class MeetingForm(forms.ModelForm):
    
    class Meta:
        model = Meeting
        fields = ['date', 'time', 'title', 'location', 'contact']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'time': forms.TimeInput(attrs={'type':'time'})
        }