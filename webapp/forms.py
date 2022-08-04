from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clean_remain(self):
        remain = self.cleaned_data.get("remain")
        if remain < 0:
            raise ValidationError("Остаток не может быть 0")
        return remain


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Find')



