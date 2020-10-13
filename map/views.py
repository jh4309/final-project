from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import sighting



def index(request):
    
    sightings = sighting.objects.all()
    context = {
            'sightings': sightings,
   
              }
    return render(request, 'map/index.html', context)

def detail(request, map_id):
    sighting = get_object_or_404(sighting, pk=map_id)

    context = {
            'sighting': sighting,
    }

    return render(request, 'map/detail.html', context)




# Create your views here.
