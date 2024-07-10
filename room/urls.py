from django.urls import path
from . import views

app_name = "room"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("create-room/", views.create_room, name="create-room"),
    path("<str:room_id>/", views.room, name="room"),
    path("update-room/<str:room_id>/", views.updateroom, name="update-room"),
    path("delete-room/<str:room_id>/", views.deleteRoom, name="delete-room"),
    path("delete-message/<str:message_id>/", views.deleteMessage, name="delete-message"),

    path("topics/", views.topicPage, name="topics"),
    path("activities/", views.activityPage, name="activities"),

]
