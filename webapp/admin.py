from django.contrib import admin

# Register your models here.
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'remaining_amount', 'price', 'category']
    list_display_links = ['id']
    list_filter = ['category']
    search_fields = ['name', 'id']
    fields = ['name', 'description', 'remaining_amount', 'price', 'category']
    readonly_fields = ['price', 'category']


admin.site.register(Product, ProductAdmin)
