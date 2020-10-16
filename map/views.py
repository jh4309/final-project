from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import sighting



def index(request):
    
    Sightings = sighting.objects.all()
    context = {
            'sightings': Sightings,
   
              }
    return render(request, 'map/index.html', context)

def detail(request, sighting_id):
    Sighting = get_object_or_404(sighting, pk=sighting_id)

    context = {
            'sighting': Sighting,
    }

    return render(request, 'map/detail.html', context)

def addsight(request):
    return render(request, 'map/addsight.html')


def sighting_request(request):
    pass


# Create your views here.
