from django.db import models

CATEGORY_CHOICES = [('Other', 'Other'), ('Clothes', 'Clothes'), ('Food', 'Food'), ('Car', 'Car'), ('Soft', 'Soft')]


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name', null=False, blank=False)
    description = models.TextField(max_length=2000, verbose_name='description', null=True, blank=True)
    remain = models.PositiveIntegerField(verbose_name='remain', null=False, blank=False)
    price = models.DecimalField(verbose_name='price', decimal_places=2, max_digits=7)
    category = models.CharField(max_length=50, verbose_name='category', null=False, blank=False,
                                default=CATEGORY_CHOICES[0][0], choices=CATEGORY_CHOICES)

    def __str__(self):
        return '{self.pk}. {self.name}: {self.price}'

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
