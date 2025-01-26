# chat/urls.py
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("time/", views.time),
    path("game/", views.game),
    path("admin/", views.admin),
    path("admin/qr/", views.qr),
    path("admin/<int:severity>/<str:hospital>/", views.time),    
    path("<str:room_name>/", views.room, name="room")
]