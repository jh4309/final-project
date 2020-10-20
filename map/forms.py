from django.forms import ModelForm

from .models import sighting 


class sightform(ModelForm):
    class Meta:
        model = sighting
        fields = [
            'latitude',
            'longitude',
            'uniquesid',
            'date',
                

                
        ]
class updateform(ModelForm):
    class Meta:
        model = sighting
        fields = [
            'latitude',
            'longitude',
            'uniquesid',
            'shift',
            'age',
            'date',
        ]
