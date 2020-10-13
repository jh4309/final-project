from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('<int:map_id>/', views.detail, name='detail'),
]
