from django.urls import path
from appstore import views

urlpatterns = [


    path('',views.home, name='home'),
    path('products/', views.catalog, name='products'),
    path("products/<slug:slug>", views.product_detail,
         name="product-detail-page")  
]

    