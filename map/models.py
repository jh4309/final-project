from django.db import models

class sighting (models.Model):
    latitude = models.DecimalField(
            max_digits=10, 
            decimal_places=4,
    )


    longitude = models.DecimalField(
            max_digits=10,
            decimal_places=4,
    )

    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = [
            (PM, ('PM')),
            (AM, ('AM')),
    ]


    shift = models.CharField(
            max_length=15,
            choices=SHIFT_CHOICES,
            default=AM,
    )


    date = models.DateField(
            help_text=('Date')
    )

    age = models.IntegerField()




# Create your models here.
