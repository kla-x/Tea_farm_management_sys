from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmer, TeaPlot, Task
from .forms import FarmerForm, TeaPlotForm, TaskForm

def farmer_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'farm_app/farmer_list.html', {'farmers': farmers})

def farmer_detail(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    tasks = farmer.tasks.all()
    plots = farmer.tea_plots.all()
    return render(request, 'farm_app/farmer_detail.html', {'farmer': farmer, 'tasks': tasks, 'plots': plots})

def plot_list(request):
    plots = TeaPlot.objects.all()
    return render(request, 'farm_app/plot_list.html', {'plots': plots})

def plot_detail(request, pk):
    plot = get_object_or_404(TeaPlot, pk=pk)
    return render(request, 'farm_app/plot_detail.html', {'plot': plot})

def task_list(request, farmer_pk):
    farmer = get_object_or_404(Farmer, pk=farmer_pk)
    tasks = farmer.tasks.all()
    return render(request, 'farm_app/task_list.html', {'tasks': tasks, 'farmer': farmer})

def create_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmer_list')
    else:
        form = FarmerForm()
    return render(request, 'farm_app/farmer_form.html', {'form': form})

def create_plot(request):
    if request.method == 'POST':
        form = TeaPlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plot_list')
    else:
        form = TeaPlotForm()
    return render(request, 'farm_app/plot_form.html', {'form': form})

def create_task(request, farmer_pk):
    farmer = get_object_or_404(Farmer, pk=farmer_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.farmer = farmer
            task.save()
            return redirect('task_list', farmer_pk=farmer.pk)
    else:
        form = TaskForm()
    return render(request, 'farm_app/task_form.html', {'form': form, 'farmer': farmer})