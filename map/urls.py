from django.urls import path

from . import views


app_name = 'Sighting'


urlpatterns = [
    path('', views.index),
    path('<str:sighting_id>/', views.detail, name='detail' ),
    path('addsight', views.addsight),
    path('request/', views.sighting_request, name='request'),
]

