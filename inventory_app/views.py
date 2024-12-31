from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def inventory_list(request):
    products = Product.objects.all()
    return render(request, 'inventory_app/inventory_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory_app/product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = ProductForm()
    return render(request, 'inventory_app/product_form.html', {'form': form})