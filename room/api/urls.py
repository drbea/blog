from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("", views.getRoutes, name = "getRoutes"),
    path("rooms/", views.getRooms, name="getRooms"),
    path("room/<str:room_id>/", views.getRoom, name="getRoom"),
]
