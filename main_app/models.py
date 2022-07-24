from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


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
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('index')

    
    



    

    




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