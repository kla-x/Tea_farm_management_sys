from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
]