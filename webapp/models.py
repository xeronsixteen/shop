from django.core.validators import MinValueValidator
from django.db import models

CATEGORY_CHOICES = [('Other', 'Other'), ('Clothes', 'Clothes'), ('Food', 'Food'), ('Car', 'Car'), ('Soft', 'Soft')]


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name', null=False, blank=False)
    description = models.TextField(max_length=2000, verbose_name='description', null=True, blank=True)
    remain = models.PositiveIntegerField(verbose_name='remain', null=False, blank=False)
    price = models.DecimalField(verbose_name='price', decimal_places=2, max_digits=7,
                                validators=(MinValueValidator(0),))
    category = models.CharField(max_length=50, verbose_name='category', null=False, blank=False,
                                default=CATEGORY_CHOICES[0][0], choices=CATEGORY_CHOICES)

    def __str__(self):
        return '{self.pk}. {self.name}: {self.price}'

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Cart(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, verbose_name='Product',
                                related_name='in_cart')
    qty = models.PositiveIntegerField(verbose_name='Quantity', default=1)

    def __str__(self):
        return f'{self.pk}. {self.product} - {self.qty}'

    class Meta:
        verbose_name = 'Product in Cart'
        verbose_name_plural = 'Products in Cart'

    def get_product_total(self):
        return self.qty * self.product.price

    @classmethod
    def get_total_price(cls):
        total = 0
        for cart in cls.objects.all():
            total += cart.get_product_total()
        return total


class Order(models.Model):
    name = models.CharField(verbose_name='name', max_length=50)
    phone = models.CharField(verbose_name='phone', max_length=40)
    address = models.CharField(verbose_name='address', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    products = models.ManyToManyField('webapp.Product', related_name='orders', verbose_name='Products',
                                      through='webapp.OrderProduct', through_fields=['order', 'product'])

    def __str__(self):
        return f'{self.pk}. {self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', verbose_name='Product', on_delete=models.CASCADE,
                                related_name='order_products')
    order = models.ForeignKey('webapp.Order', verbose_name='Order', on_delete=models.CASCADE,
                              related_name='order_products')
    qty = models.PositiveIntegerField(verbose_name='Quantity')

    def __str__(self):
        return f'{self.pk}. {self.product.name} - {self.order.name}'

    class Meta:
        verbose_name = 'Product in Order'
        verbose_name_plural = 'Products in Order'
