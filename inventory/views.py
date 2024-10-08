from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login

from .forms import ProductForm, UserForm
from .models import Product, Price, Dimension, Characteristic

def redirectHome(request):
    return redirect('inventory:home')

def createProduct(request):

    if request.method == 'POST':

        form = ProductForm( request.POST )

        if form.is_valid():
            product = form.save(commit=False)
            price_product = form.cleaned_data['price']
            height_product = form.cleaned_data['height']
            width_product = form.cleaned_data['width']
            color_product = form.cleaned_data['color']
            material_type_product = form.cleaned_data['material_type']


            product.save()

            price = Price(product=product, amount=price_product)
            dimension = Dimension( height=height_product, width=width_product )
            characteristic = Characteristic(product=product, dimension=dimension, color=color_product, material_type=material_type_product)

            price.save()
            dimension.save()
            characteristic.save()
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
    characteristic = Characteristic.objects.filter(product=product).first()
    dimension = Dimension.objects.filter( characteristic=characteristic ).first()

    if request.method == 'POST':
        product_form = ProductForm( request.POST, instance=product )
        product_form.save()

        price.amount = product_form.cleaned_data['price']
        price.save()

        dimension.height = product_form.cleaned_data['height']
        dimension.width = product_form.cleaned_data['width']
        dimension.save()

        characteristic.color = product_form.cleaned_data['color']
        characteristic.material_type = product_form.cleaned_data['material_type']
        characteristic.save()

        return redirect('inventory:home')
    else: 
        product_form = ProductForm(initial={ 
            'price':price.amount,
            'height':dimension.height,
            'width':dimension.width,
            'color': characteristic.color,
            'material_type':characteristic.material_type
              }, instance=product )

    return render(request, 'inventory/edit.html',{'product_form':product_form} )

def orderProducts(request, characteristic):
    products_with_price = []
    products = Product.objects.order_by(characteristic)[:20]
    for product in products:
        price = Price.objects.filter(product=product).first()
        products_with_price.append({
            'product':product,
            'price': price.amount if price else None
        })    
    return render(request, 'inventory/home.html', {'products_with_price':products_with_price})

def filterProducts(request, filters):
    
    print(filters)
    return JsonResponse('Todo ok')


def register(request):

    if request.method == 'POST':
        form = UserForm( request.POST or None )
        if form.is_valid():
            new_user = form.save()
            login( request, new_user )
            return redirect('inventory:home')
    else:
        form = UserForm()
    
    return render( request, 'registration/register.html', {'form': form } )