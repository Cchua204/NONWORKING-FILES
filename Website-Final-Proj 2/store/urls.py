from django.contrib import admin
from django.urls import include, path
from appstore import views

urlpatterns = [
    path("", include("appstore.urls")),
    path('admin/', admin.site.urls),
    path('', include('quotations.urls')),
    path('customers/',include('quotations.urls')),
    path('customer/<str:customer_id>/', views.my_view, name='view_customer'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
]
