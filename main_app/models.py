from django.db import models

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