from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductForm
from webapp.models import Product


# Create your views here.


def index(request):
    products = Product.objects.order_by('name')
    context = {'products': products}
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = ProductForm
        return render(request, "create.html", {'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            price = form.cleaned_data.get('price')
            remain = form.cleaned_data.get('remain')
            new_product = Product.objects.create(name=name, description=description, price=price, remain=remain)
            return redirect('index')
        return render(request, 'create.html', {'form': form})


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'remain': product.remain

        })
        return render(request, "update.html", {'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect('index')
        return redirect('index', {'form': form})


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, "delete.html", {"product": product})
    else:
        product.delete()
        return redirect('index')


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, "product_view.html", {"product": product})


