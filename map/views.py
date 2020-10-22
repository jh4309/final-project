from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import sighting
from .forms import updateform
from .forms import sightform
import random

def index(request):
    
    sights = sighting.objects.all()
    fields = ['uniquesid','longitude','latitude','Date','shift']
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

    return render(request, 'map/update.html', context)

def homepage(request):
    return render(request,'map/homepage.html')

def stats(request):
    Sighting = sighting.objects.all()
    adult_c = 0
    running_c = 0
    eating_c = 0
    chasing_c = 0
    foraging_c = 0
    
    for s in Sighting:
        if s.age == "Adult":
            adult_c+=1
        if s.Running == True:
            running_c+=1
        if s.Chasing == True:
            chasing_c+=1
        if s.Eating == True:
            eating_c+=1
        if s.Foraging == True:
            foraging_c+=1
    context={
            'AdultCounts':adult_c,
            'NumofRunning':running_c,
            'NumofChasing':chasing_c,
            'NumofEating':eating_c,
            'NumofForaging':foraging_c,
            }

    return render(request,'map/stats.html',context)

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


def sighting_details(request,sighting_id):
    sights = get_object_or_404(sighting, uniquesid=sighting_id)
    context = {
            'sights':sights
            }
    
    return render(request, 'map/detail.html', context)

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
