from django import forms
from .models import Farmer, TeaPlot, Task

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'contact_information']

class TeaPlotForm(forms.ModelForm):
    class Meta:
        model = TeaPlot
        fields = ['name', 'location', 'area', 'soil_type', 'number_of_plants', 'farmer']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'farmer']