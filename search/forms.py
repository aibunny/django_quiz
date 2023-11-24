from django import forms

class PassengerSearchForm(forms.Form):
    name = forms.CharField(required=False, label= "Name")