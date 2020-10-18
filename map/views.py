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
    if request.method == 'POST':
        form = addsightingform(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)

def map(request):
    return render(request, 'map/map.html', {})
# Create your views here.
