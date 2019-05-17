from django import forms
from  .models import PersonalDate
class PersonalDateForm(forms.Form):
    class Meta:
        model= PersonalDate
        fileds = ['full_name',' age','city','profesion','problem ','reabilitations_type','diseases']