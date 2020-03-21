from django.contrib.auth.forms import UserCreationForm
from django import forms
from django_common.auth_backends import User
from ASR_Main.models import profile
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class UserSignupForm(UserCreationForm):
    CHOICES = [
        ('G', 'Guest'),
        ('E', 'Upwork'),
        ('F', 'Freelance'),
        ('C', 'Colleague')
    ]
    clienttype1 = forms.CharField(required=True, widget=forms.Select(choices=CHOICES), label="User Type")
    country = CountryField(blank_label='--Select country--').formfield()
    phonenumber1 = PhoneNumberField().formfield(label="Phone Number")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'clienttype1', 'password1', 'password2', 'country',
                  'phonenumber1']
