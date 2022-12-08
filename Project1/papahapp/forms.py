from django import forms
from .models import *

class BreachForm(forms.ModelForm):

    #meta class with the fields
    class Meta:
        model = Breach
        fields = ['first_name', 'last_name', 'breach_num', 'street_address', 'apt_number', 'city', 'state_abbreviation', 'zipcode', 'email', 'phone', 'breach_type', 'breach_description']
        labels = {
         
            'first_name': ('First Name'),
            'last_name' : ('Last Name'),
            'breach_num' : ('Breach Number'),
            'street_address' : ('Street Address'),
            'apt_number' : ('Apt Number'),
            'city' : ('City)'),
            'state_abbreviation' : ('State)'),
            'zipcode' : ('Zip'),
            'email' : ('Email'),
            'phone' : ('Phone'),
            'breach_type' : ('Breach Type'),
            'breach_description' : ('Description'),
        }