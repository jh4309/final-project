from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import sighting
from .forms import updateform
from .forms import sightform
import random

def index(request):
    
    sights = sighting.objects.all()
    fields = ['uniquesid','longitude','latitude','date','shift']
    context = {
            'sights': sights,
            'fields': fields
              }
    return render(request, 'map/index.html', context)

def update_sights(request, sighting_id):
    Sighting = sighting.objects.get(uniquesid=sighting_id)
    if request.method == 'POST':
        form = updateform(request.POST,instance = Sighting)
        if form.is_valid():
            form.save()
            return redirect(f/'sightings')
    else:
        form =updateform(instance = Sighting)
    context = {
            'form': form,
    }

    return render(request, 'map/detail.html', context)

def addsight(request):
    if request.method == 'POST':
        form = sightform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f/'sightings')
    else:
        form = sightform()
    context = {
            'form':form,
            }

    return render(request, 'map/addsight.html', context)


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
    sights = sighting.objects.all()
    new_list = []
    for i in range(100):
        chosen = random.choice(sights)
        new_list.append(chosen)
    sights = new_list
    context = {
            'sights': sights,
            }
    return render(request, 'map/map.html',context)
# Create your views here.
