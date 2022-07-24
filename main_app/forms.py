from unittest import case
from django import forms
from django.forms import ModelForm
from main_app.models import  Keyboard
# from django.core.exceptions import ValidationError



class KeyboardForm(ModelForm):

    class Meta:
        model = Keyboard
        fields = '__all__'

    # def clean_field(self):
    #     value = self.cleaned_data['field']
    #     if value == 'ashish':
    #         raise ValidationError('ashish is not alloved here.')
    #     return value
        
    
