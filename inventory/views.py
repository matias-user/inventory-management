from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product, Price

# Create your views here.
def home(request):

    products = Product.objects.all()
    print(products[4])
    return render(request, 'inventory/home.html' )


def createProduct(request):

    if request.method == 'POST':

        form = ProductForm( request.POST )

        if form.is_valid():
            product = form.save(commit=False)
            price_product = form.cleaned_data['price']
            product.save()

            price = Price(product=product, amount=price_product)
            price.save()

            return redirect('inventory:home')
    else:
        form = ProductForm()


    return render(request, 'inventory/createProduct.html',{"form":form})