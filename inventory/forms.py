from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    sku = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )
    brand = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )

    
    class Meta:
        model = Product
        fields = '__all__'

