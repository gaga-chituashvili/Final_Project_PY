from django.shortcuts import render
from myapp.models import Product 
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_view(request):
    return render(request, "home.html")


def product_view(request):
    return render(request,"product.html",
                  {
        "products": Product.objects.all()  
    })


def details_view(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,"details.html",{
        "product" : product
    })


