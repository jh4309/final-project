from django.forms import ModelForm

from .models import sighting 


class addsightingform(ModelForm):
    class Meta:
        model = sighting
        fields = [
            'latitude',
            'longitude',
            'date',


                
        ]
