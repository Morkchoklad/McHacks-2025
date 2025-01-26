# chat/urls.py
from django.urls import path, re_path
from chat.views import chat_box
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("time/", views.time),
    path("game/", views.game),
    path("admin/", views.admin),
    path("admin/qr/", views.qr),
    path("admin/<int:severity>/<str:hospital>/", views.time),    
    path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
]