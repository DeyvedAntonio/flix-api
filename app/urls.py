from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreListCreateView.as_view(), name='genres-creat-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genres-detail-update-destroy'),
    path('actors/', ActorListCreateView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actors-detail-update-destroy'),
]
