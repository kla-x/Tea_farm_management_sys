from django.shortcuts import render
from farm_app.models import Farmer, TeaPlot, Task
from inventory_app.models import Product
from sales_app.models import Customer, Sale
from employee_app.models import Employee

def employee_records(request):
    employees = Employee.objects.all()
    return render(request, 'records_app/employee_records.html', {'employees': employees})

def farm_records(request):
    farmers = Farmer.objects.all()
    plots = TeaPlot.objects.all()
    return render(request, 'records_app/farm_records.html', {'farmers': farmers, 'plots': plots})

def harvest_records(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'records_app/harvest_records.html', {'tasks': tasks})

def inventory_records(request):
    products = Product.objects.all()
    return render(request, 'records_app/inventory_records.html', {'products': products})

def sales_records(request):
    sales = Sale.objects.all()
    customers = Customer.objects.all()
    return render(request, 'records_app/sales_records.html', {'sales': sales, 'customers': customers})