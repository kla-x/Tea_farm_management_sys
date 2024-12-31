from django.contrib import admin

# Register your models here.
from .models import Sale, Customer


admin.site.register(Sale)
admin.site.register(Customer)