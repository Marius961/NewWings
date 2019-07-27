from django import forms
from django.forms import TextInput,NumberInput,RadioSelect

from .models import Suport


class SuportForm(forms.ModelForm):
    class Meta:
        model = Suport
        fields = ["full_name", "age",  "city","problem", "live_through","reabil_type","recent_treatment",
                  "exemption"]
        widgets = {'full_name': TextInput(attrs={'class': 'form-control'}),
                   'age': NumberInput(attrs={'class': 'form-control'} ),
                   'city': TextInput(attrs={'class': 'form-control'}),
                   'problem': TextInput(attrs={'class': 'form-control'}),
                   'live_through': TextInput(attrs={'class': 'form-control'}),
                   'recent_treatment': TextInput(attrs={'class': 'form-control'}),
                   'reabil_type': TextInput(attrs={'class': 'form-control'}),
                   'exemption': RadioSelect (attrs={'class': 'form-control'})}
