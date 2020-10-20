from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import sighting
from .forms import updateform
from .froms import sightform


def index(request):
    
    sights = sighting.objects.all()
    fields = ['uniquesid','longitude','latitude','date','shift']
    context = {
            'sights': sights,
            'fields': fields
              }
    return render(request, 'map/index.html', context)

def update_sights(request, uniquesid):
    Sighting = sighting.object.get(uniquesid=uniquesid)
    if request.method == 'POST':
        form = updateform(request.POST,instance = sighting)
        if form.is_valid():
            form.save()
            return redirect(f/'sightings')
    else:
        form =updateform(instance = sighting)
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
        else
            form = sightform
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
    sights = sighting.object.all()[:100]
    context = {
            'sights': sights,
            }
    return render(request, 'map/map.html',context)
# Create your views here.
