from django.db import models

class sighting (models.Model):


    latitude = models.FloatField(
            null=True
    )


    longitude = models.FloatField(
            null=True
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


    date = models.CharField(
            max_length=16,
            default=('mmddyyyy'),
    )

    

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'
    UNKNOWN = 'UNKNOWN'


    AGE_CHOICES = [
            (ADULT, ('Adult')),
            (JUVENILE, ('Juvenile')),
            (UNKNOWN, ('?')),
    ]

    age = models.CharField(
            max_length=20,
            choices = AGE_CHOICES,
            help_text=('Age of squirrel'),
            default = ADULT
    )

    
    uniquesid = models.CharField(
            max_length=20,
            default=('DL-SF-DDDD-DD'),
    )

    def __str__(self):
        return self.uniquesid


class sightshow (models.Model):
        
    sighting = models.ForeignKey(
            'map.sighting',
            on_delete=models.CASCADE,
    )





# Create your models here.
