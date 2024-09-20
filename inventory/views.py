from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import ProductForm
from .models import Product, Price



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


def listProduct(request):

    products_with_price = []
    products = Product.objects.all()[:20]
    for product in products:
        price = Price.objects.filter(product=product).first()

        products_with_price.append({
            'product':product,
            'price': price.amount if price else None
        })    
    return render(request, 'inventory/home.html',{'products_with_price':products_with_price})


def deleteProduct(request, product):

    return JsonResponse({'redirect_url':'/home/'})