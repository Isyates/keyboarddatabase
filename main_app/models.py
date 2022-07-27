from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# from django.config import settings

# Create your models here.
COLORS = (
    ('BLA','Black'),
    ('RED', "Red"),
    ('WHI', 'White')
)

CASE_MATERIALS = (
    ('PLA','Plastic'),
    ('POLY', "Polycarbonate"),
    ('ALU', 'Aluminum'),
)

CASE_SIZE = (
    ('100','Full Size'),
    ('80', "TKL"),
    ('75', '75%'),
    ('65','65%'),
    ('60', "60%"),
    ('40', '45%'),
)

CASE_LAYOUT = (
    ('ANSI','ANSI'),
    ('ISO', "Isometric"),
    ('ORTHO', 'Ortholinear'),
)

PLATE_MATERIAL = (
    ('ALU','Aluminum'),
    ('BRA', "Brass"),
    ('ORTHO', 'Ortholinear'),
)

SWITCH_STYLE = (
    ('CLI','Clicky'),
    ('SIL', "Silent"),
    ('LIN', 'Linear'),
    ('TAC', 'Tactile'),
    ('OPT', 'Optical'),
)

TRUE_FALSE = (
    ('TRUE','Yes'),
    ('FALSE', "No"),
)


class Keyboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    Case_Color = models.CharField(
        max_length=20,
        choices = COLORS,
        default= 'BLA'
        )
    Case_Material = models.CharField(
        max_length = 20,
        choices = CASE_MATERIALS,
        default='ALU'
        )
    Case_Size = models.CharField(
        max_length=20,
        choices = CASE_SIZE,
        default='100'
        )
    
    Case_Layout = models.CharField(
        max_length= 20,
        choices = CASE_LAYOUT,
        default='ANSI'
        )
    Plate_Name = models.CharField(
        max_length= 20,
        default = 'Glorious'
        )
    Plate_Color = models.CharField(
        max_length= 20,
        choices = COLORS,
        default='BLA'
        )
    Plate_Material = models.CharField(
        max_length= 20,
        choices = PLATE_MATERIAL,
        default='ALU'
        )
    Switch_Name = models.CharField(
        max_length= 20,
        default = 'Cherry MX'
        )
    Switch_Color = models.CharField(
        max_length= 20,
        choices = COLORS,
        default='BLA'
        )
    Switch_Style = models.CharField(
        max_length= 20,
        choices = SWITCH_STYLE,
        default='LIN'
        )
    Switch_RGB = models.CharField(
        max_length= 20,
        choices = TRUE_FALSE,
        default='TRUE'
        )
    Keycap_Name = models.CharField(
        max_length= 20,
        default = 'GMK'
        )
    Keycap_Color = models.CharField(
        max_length= 20,
        choices = COLORS,
        default='BLA'
        )
    Keycap_Legend = models.CharField(
        max_length= 20,
        choices = TRUE_FALSE,
        default='TRUE'
        )
    Keycap_Shinethrough = models.CharField(
        max_length= 20,
        choices = TRUE_FALSE,
        default='TRUE'
        )

    
    def __str__(self):
        return self.name

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('keyboards_index')

    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request,user)
        return redirect('index')
    else:
        error_message = "invalid sign-up, please try again."
    form = UserCreationForm()
    context = {"form": form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)




    

    




    # Create your models here.


#Keyboard model

#Case model with foreign key to keyboard
    # properties
        # name:
        # color:
        # material: 'plastic', 'polycarbonate', 'aluminum', 'acrylic', 'wood'
        # size : '100%/Full Sized', '80%/TKL', '75%', '65%', '60%', '40%'
        # layout: 'ANSI', 'ISO', 'Ortholinear'

# Plate model with foreign key to keyboard
    # properties
        # name
        # color
        # material: 'aluminium', 'brass', 'polycarbonate', 'steel', 'carbon fiber'

# switches model with foreign key to keyboard
    # properties
        # name
        # color:
        # switchstyle: 'clicky', 'silent', 'linear','tactile', 'optical'
        # RGB: (Y/N)


#keycaps model with foreign key to keyboard
    # Properties
        # name
        # color:
        # legend: (Y/N)
        # backlight_Shinethrough: (Y/N)