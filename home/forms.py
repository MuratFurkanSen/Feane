from django.forms import ModelForm, TextInput, DateInput, EmailInput, Select

from home.models import Reservation


class RegistrationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'phone', 'email', 'person_Count', 'date']
        widgets = {
            'full_name': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'phone': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'email': EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'person_Count': Select(attrs={'class': 'form-control nice-select wide'},
                                   choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
            'date': DateInput(
                attrs={'class': 'form-control', 'type': 'date'})
        }

