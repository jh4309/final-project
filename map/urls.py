from django.urls import path

from . import views


app_name = 'Sighting'


urlpatterns = [
    path('sightings', views.index),
    path('sightings/<uniquesid>/', views.update_sights),
    path('sightings/add', views.addsight),
    path('map',views.map,name='map'),
]

