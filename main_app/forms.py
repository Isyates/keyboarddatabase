
from django.forms import ModelForm
from main_app.models import  Keyboard




class KeyboardForm(ModelForm):
    class Meta:
        model = Keyboard
        fields = ['name','description']

   
