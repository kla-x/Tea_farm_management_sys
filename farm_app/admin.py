from django.contrib import admin

from .models import Farmer, TeaPlot, Task

admin.site.register(Farmer)
admin.site.register(TeaPlot)
admin.site.register(Task)
