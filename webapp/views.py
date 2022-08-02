from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product


# Create your views here.


class ProductListView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Product.objects.filter(
                Q(name__icontains=self.search_value)) | Q(description__icontains=self.search_value)
        return Product.objects.filter(remain__gte='2').order_by('category', 'name')

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


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
