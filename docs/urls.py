from django.urls import path
from . import views

urlpatterns = [
    path("trailers/", views.trailers, name="trailers"),
    path("tractors/", views.tractors, name="tractors")
]