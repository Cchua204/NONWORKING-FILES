from django.urls import path
from appstore import views
from django.contrib import admin
from django.http import HttpResponse

def quotations(request):
    return HttpResponse('request page')

urlpatterns = [
    path("", views.home, name="appstore"),
    path('quotations/', quotations)
]
