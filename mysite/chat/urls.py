# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("time/", views.time),
    path("game/", views.game),
    path("admin/", views.admin),
    path("<str:room_name>/", views.room, name="room")
]