from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Sale
from .forms import CustomerForm, SaleForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'sales_app/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    sales = customer.sale_set.all()
    return render(request, 'sales_app/customer_detail.html', {'customer': customer, 'sales': sales})

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales_app/sale_list.html', {'sales': sales})

def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales_app/sale_detail.html', {'sale': sale})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'sales_app/customer_form.html', {'form': form})

def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'sales_app/sale_form.html', {'form': form})