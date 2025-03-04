from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorListCreateView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>', views.ActorRetrieveUpdateDestroyView.as_view(), name='actors-retrive-update-destroy'),
]