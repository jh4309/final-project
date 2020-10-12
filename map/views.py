from django.shortcuts import render

from .models import sighting



def index(request):
    
    sightings = sighting.objects.all()
    context = {
            'sightings': sightings,


    return render(request, 'map/index.html', context)

# Create your views here.
