from django.urls import path

from webapp.views import ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name="update"),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="delete"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_view")

]