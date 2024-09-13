from django.shortcuts import render
from .forms import ProductForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):

    return render(request, 'inventory/home.html' )


def createProduct(request):

    if request.method == 'POST':

        form = ProductForm( request.POST )

        if form.is_valid():
            print( request.POST )
            return HttpResponseRedirect("Gracias!")
    else:
        form = ProductForm()


    return render(request, 'inventory/createProduct.html',{"form":form})