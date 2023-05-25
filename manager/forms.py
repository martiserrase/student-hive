from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form

from manager.models import (Profile, Event, MaintenanceRequest)


class NewUserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ("username",
                  "email",
                  "first_name",
                  "last_name",
                  "room",
                  "id_number",
                  "initial_contract_date",
                  "final_contract_date",
                  "password1",
                  "password2")


class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name',
                  'description',
                  'location',
                  'date',
                  'hour']
        widgets = {'date': DateInput()}


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['title',
                  'description',
                  'relevance']


# Class ContractForm IS NOT WORKING, it doesn't cause problems but it doesn't work
class ContractForm(Form):
    user_name = forms.CharField(label='User name', max_length=100)
