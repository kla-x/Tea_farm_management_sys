from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_app/employee_detail.html', {'employee': employee})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_app/employee_form.html', {'form': form})