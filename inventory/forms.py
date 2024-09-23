from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    sku = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )
    brand = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )
    description = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control form-control-sm','rows':'3'}) )
    height = forms.FloatField( widget=forms.HiddenInput() )
    weight = forms.FloatField( widget=forms.HiddenInput() )
    color = forms.CharField(widget=forms.HiddenInput())
    material_type = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Product
        fields = '__all__'

