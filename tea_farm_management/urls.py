"""
URL configuration for tea_farm_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('farm/', include('farm_app.urls')),
    path('inventory/', include('inventory_app.urls')),
    path('sales/', include('sales_app.urls')),
    path('employees/', include('employee_app.urls')),
    path('records/', include('records_app.urls')),
    # path('', RedirectView.as_view(url='/farm/', permanent=False), name='home'),  # Redirect root URL to '/farm/'
    path('', views.base_landing, name='base_landing'),
]