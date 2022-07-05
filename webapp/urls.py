from django.urls import path

from webapp.views import index, create, update, delete, product_view

urlpatterns = [
    path('', index, name='index'),
    path('product/add/', create, name='create'),
    path('product/<int:pk>/update', update, name="update"),
    path('product/<int:pk>/delete', delete, name="delete"),
    path('product/<int:pk>/', product_view, name="product_view")

]