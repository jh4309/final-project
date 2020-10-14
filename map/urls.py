from django.urls import path

from . import views


app_name = 'Sighting'


urlpatterns = [
    path('', views.index),
    path('<int:sighting_id>/', views.detail, name='detail', ),
]

