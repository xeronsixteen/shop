from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import ProductForm
from webapp.models import Product


# Create your views here.


class ProductListView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().order_by('category', 'name')


class ProductCreateView(CreateView):
    template_name = 'create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={"pk": self.object.pk})


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    template_name = 'update.html'
    model = Product

    def get_success_url(self):
        return reverse('product_view', kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_view.html'
    success_url = reverse_lazy('product_view')
