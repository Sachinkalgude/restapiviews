from django.urls import path
from .views import *
urlpatterns = [
    path("home/",home,name="home"),
    path("home/<int:id>/",home,name="home"),
]
