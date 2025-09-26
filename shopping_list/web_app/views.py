from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def adauga(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'adauga.html', {'form': form})

def sterge(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('home')

def marcheaza_cumparat(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.bought = True
    product.save()
    return redirect('home')
