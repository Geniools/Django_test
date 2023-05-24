from django.urls import path

from . import views

urlpatterns = [
    path("<str:n>/", views.index, name="index"),
]