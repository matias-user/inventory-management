from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    price = forms.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'

