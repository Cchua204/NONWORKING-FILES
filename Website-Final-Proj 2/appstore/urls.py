from django.urls import path
from appstore import views

urlpatterns = [
    path("home/", views.home, name="appstore"),
]