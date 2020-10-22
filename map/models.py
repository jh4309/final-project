from django.db import models
from django.utils.translation import gettext as _


class sighting (models.Model):


    latitude = models.FloatField(
            null=True,
    )


    longitude = models.FloatField(
            null=True,
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
        auto_now = False,
        auto_now_add = False,
        help_text=_('yyyy-mm-dd'),
        
    )

    

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'
    UNKNOWN = 'UNKNOWN'


    AGE_CHOICES = [
            (ADULT, ('Adult')),
            (JUVENILE, ('Juvenile')),
            (None, ''),
            (UNKNOWN, ('?')),
    ]

    age = models.CharField(
            max_length=20,
            choices = AGE_CHOICES,
            help_text=('Age of squirrel'),
            blank = True,
    )

    
    uniquesid = models.CharField(
            max_length=25,
        
    )
    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'

    COLOR_CHOICE=(
            (Black, 'Black'),
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            (None, ''),
            )

    Primary_Fur_Color = models.CharField(
            help_text = _('Fur color'),
            max_length=16,
            choices = COLOR_CHOICE,
            blank = True,
            )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    LOCATION_CHOICE=(
            (Ground_Plane, 'Ground Plane'),
            (Above_Ground, 'Above Ground'),
            (None, ''),
            )

    Location =  models.CharField(
            help_text = _('Location'),
            max_length=128,
            choices = LOCATION_CHOICE,
            blank = True,
            )

    Specific_Location = models.CharField(
            help_text = _('Additional notes to the location'),
            max_length=128,
            blank = True,
            )

    Running = models.BooleanField(
            help_text = _('Running'),
            blank=True,  
            null = True,
    )

    Chasing = models.BooleanField(
            help_text = _('Chasing'),
            blank=True,
            null = True,
    )

    Climbing = models.BooleanField(
            help_text = _('Climbing'),
            blank=True,
            null = True,
    )

    Eating = models.BooleanField(
            help_text = _('Eating'),
            blank=True,
            null = True,
    )

    Foraging = models.BooleanField(
            help_text = _('Foraging'),
            blank=True,
            null = True,
    )

    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        max_length = 128,
        null = True,
        blank = True
    )

    Kuks = models.BooleanField(
            help_text = _('Kuks'),
            blank=True,
            null = True,
    )

    Quaas = models.BooleanField(
            help_text = _('Quaas'),
            blank=True,
            null = True,
    )

    Moans = models.BooleanField(
            help_text = _('Moans'),
            blank=True,
            null = True,
    )

    Tail_Flags = models.BooleanField(
            help_text = _('Tail_Flags'),
            blank=True,
            null = True,
    )

    Tail_Twitches = models.BooleanField(
            help_text = _('Tail_Twitches'),
            blank=True,
            null = True,
    )

    Approaches = models.BooleanField(
            help_text = _('Approaches'),
            blank=True,
            null = True,
    )

    Indifferent = models.BooleanField(
            help_text = _('Indifferent'),
            blank=True,
            null = True,
    )

    Runs_From = models.BooleanField(
            help_text = _('Runs_From'),
            blank=True,
            null = True,
    )

    def __str__(self):
        return self.uniquesid


class sightshow (models.Model):
        
    sighting = models.ForeignKey(
            'map.sighting',
            on_delete=models.CASCADE,
    )





# Create your models here.
