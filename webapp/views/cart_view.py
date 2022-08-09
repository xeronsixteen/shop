from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from webapp.forms import CartForm, OrderForm
from webapp.models import Cart, Product, Order, OrderProduct


class CartAddView(CreateView):
    model = Cart
    form_class = CartForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        qty = form.cleaned_data.get('qty')
        if qty > product.remain:
            raise ('Product does not exist')
        else:
            # try:
            #     cart_product = Cart.objects.get(product=product)
            #     cart_product.qty += qty
            #     cart_product.save()
            # except Cart.DoesNotExist:
            #     Cart.objects.create(product=product, qty=qty)
            cart_product, is_created = Cart.objects.get_or_create(product=product)
            if is_created:
                cart_product.qty = qty
            else:
                cart_product.qty += qty
            cart_product.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class CartListView(ListView):
    model = Cart
    template_name = 'cart/cart-listview.html'
    context_object_name = 'carts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['total'] = Cart.get_total_price()
        context['form'] = OrderForm()
        return context


class CartDeleteView(DeleteView):
    model = Cart
    success_url = reverse_lazy('webapp:cart')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CartDeleteByOneView(DeleteView):
    model = Cart
    success_url = reverse_lazy('webapp:cart')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        cart = self.object
        cart.qty -= 1
        if cart.qty < 1:
            cart.delete()
        else:
            cart.save()
        return HttpResponseRedirect(success_url)


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('webapp:index')

    # def form_valid(self, form):
    #     order = form.save()
    #
    #     for item in Cart.objects.all():
    #         OrderProduct.objects.create(product=item.product, qty = item.qty, order=order)
    #         item.product.remain -= item.qty
    #         item.product.save()
    #         item.delete()
    #     return HttpResponseRedirect(self.success_url())

    def form_valid(self, form):
        print(form)
        order = form.save()

        products = []
        order_products = []

        for item in Cart.objects.all():
            order_products.append(OrderProduct(product=item.product, qty=item.qty, order=order))
            item.product.remain -= item.qty
            products.append(item.product)

        OrderProduct.objects.bulk_create(order_products)
        Product.objects.bulk_update(products, ("remain",))
        Cart.objects.all().delete()
        return HttpResponseRedirect(self.success_url)


