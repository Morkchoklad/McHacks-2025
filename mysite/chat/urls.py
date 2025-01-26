# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat),
    path("", views.admin),
    path("time/", views.time),
    path("game/", views.game),
    path("admin/", views.admin),
    path("admin/qr/", views.qr),
    path("admin/<int:severity>/<str:hospital>/", views.time),
    path('send_message/<str:message>/<str:user>', views.send_message),

]