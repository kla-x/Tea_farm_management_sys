from django.shortcuts import render, redirect

def base_landing(request):
    
    return render(request, 'base_nav.html')