from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_records, name='employee_records'),
    path('farms/', views.farm_records, name='farm_records'),
    path('harvests/', views.harvest_records, name='harvest_records'),
    path('inventory/', views.inventory_records, name='inventory_records'),
    path('sales/', views.sales_records, name='sales_records'),
]