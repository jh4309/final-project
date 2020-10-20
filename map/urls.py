from django.urls import path

from . import views


app_name = 'Sighting'


urlpatterns = [
    path('sightings', views.index),
    path('sightings/<str:sighting_id>/', views.update_sights),
    path('sightings/add', views.addsight),
    """path('sightings/request/', views.sighting_request, name='request'),"""
    path('map',views.map,name='map'),
]

