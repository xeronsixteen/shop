from django.urls import path

from webapp.views import CartAddView, CartListView, CartDeleteView, CartDeleteByOneView, CreateOrderView
from webapp.views.product_view import ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name="update"),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="delete"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_view"),
    path('product/<int:pk>/add-to-cart/', CartAddView.as_view(), name="add_to_cart"),
    path('cart/', CartListView.as_view(), name="cart"),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name="delete_from_cart"),
    path('cart/<int:pk>/delete_by_one/', CartDeleteByOneView.as_view(), name="delete_one_from_cart"),
    path('order/create/', CreateOrderView.as_view(), name="create_order"),


]

