from django.urls import path
from . import views

urlpatterns = [
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('farmers/<int:pk>/', views.farmer_detail, name='farmer_detail'),
    path('plots/', views.plot_list, name='plot_list'),
    path('plots/<int:pk>/', views.plot_detail, name='plot_detail'),
    path('farmers/<int:farmer_pk>/tasks/', views.task_list, name='task_list'),
    path('farmers/create/', views.create_farmer, name='create_farmer'),
    path('plots/create/', views.create_plot, name='create_plot'),
    path('farmers/<int:farmer_pk>/tasks/create/', views.create_task, name='create_task'),
]