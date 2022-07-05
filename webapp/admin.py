from django.contrib import admin

# Register your models here.
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'category']
    list_display_links = ['id']
    list_filter = ['category']
    search_fields = ['name', 'id']
    fields = ['name', 'description', 'remain', 'price', 'category']


admin.site.register(Product, ProductAdmin)
