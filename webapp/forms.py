from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Name')
    description = forms.CharField(max_length=500, required=True, label='Text',
                                  widget=widgets.Textarea(attrs={"cols": 40,
                                                                 "rows": 3}))
    remain = forms.IntegerField(min_value=0, required=True)
    price = forms.DecimalField(decimal_places=2, max_digits=7, required=True)
    category = forms.ChoiceField(required=True, choices=CATEGORY_CHOICES)
