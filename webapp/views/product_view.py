from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.views.base_view import SearchView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductListView(SearchView):
    model = Product
    template_name = 'product/index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']
    paginate_by = 6
    context_object_name = 'products'

    def get_queryset(self):
        return super().get_queryset().filter(remain__gt=0)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_view.html'
    queryset = Product.objects.filter(remain__gt=0)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
