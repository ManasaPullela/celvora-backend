from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'index.html')
