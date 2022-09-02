from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mision/', views.mision, name='mision'),
    
]
