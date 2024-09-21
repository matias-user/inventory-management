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


def deleteProduct(request, product_id):

    product = Product.objects.get(id=product_id)
    product.delete()

    return JsonResponse({'redirect_url':'/home/'})


def editProduct(request, product_id):

    product = Product.objects.get(id=product_id)
    price = Price.objects.filter(product=product).first()

    if request.method == 'POST':
        product_form = ProductForm( request.POST, instance=product )
        product_form.save()
        
        price.amount = product_form.cleaned_data['price']
        price.save()
        return redirect('inventory:home')
    else: 
        product_form = ProductForm(initial={'price':price.amount}, instance=product )

    return render(request, 'inventory/edit.html',{'product_form':product_form} )