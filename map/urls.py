from django.urls import path

from . import views


app_name = 'map'

urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('sightings', views.index, name='sightings'),
    path('sightings/details/<str:sighting_id>',views.sighting_details, name='detail'),
    path('sightings/stats',views.stats, name='stats'),
    path('sightings/<sighting_id>/', views.update_sights),
    path('sightings/add', views.addsight),
    path('map',views.map,name='map'),
]

