from django.urls import path
from . import views

urlpatterns = [
    path('quotations/', views.quotations, name='quotations'),
    path('customers', views.customers, name='customers')
]