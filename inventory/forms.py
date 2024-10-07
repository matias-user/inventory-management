from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )
    description = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control form-control-sm','rows':'3'}) )
    sku = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )
    brand = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}) )
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    height = forms.FloatField( widget=forms.HiddenInput() )
    width = forms.FloatField( widget=forms.HiddenInput() )
    color = forms.CharField(widget=forms.HiddenInput())
    material_type = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Product
        fields = '__all__'


class UserForm( UserCreationForm ):
    username = forms.CharField( widget=forms.TextInput( attrs={'class':'form-control'} ))
    password1 = forms.CharField( widget=forms.PasswordInput( attrs={'class':'form-control'} ))
    password2 = forms.CharField( widget=forms.PasswordInput( attrs={'class':'form-control'} ))
    email = forms.CharField( widget=forms.EmailInput(attrs={'class':'form-control'}) )

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2',]