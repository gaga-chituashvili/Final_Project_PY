import random
from string import ascii_lowercase
from django.shortcuts import render
from myapp.models import Product
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView,UpdateView,DetailView,DeleteView,ListView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


fake_product_names = [
    "California rolls",
    "Dijon mustard",
    "Lebanon bologna",
]

# Create your views here.
def home_view(request):
    return render(request, "home.html")


# def product_view(request):
#     return render(request,"product.html",
#                   {
#         "products": Product.objects.all() 
#     })

def product_view(request):
    product_list = Product.objects.all() 
    paginator = Paginator(product_list, 5)  

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  
    return render(request, "product.html", {
        "products": page_obj  
    })


@login_required
def generate_random_product_view(request):
    Product.objects.create(
        thumbnil="/final_project_python/foodimg10.png",
        descriptions="".join(random.choices(ascii_lowercase, k=100)),  
        price=random.randint(10, 2000)
    )

    return redirect("myapp:products")



def details_view(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,"details.html",{
        "product" : product
    })




class ProductListenView(LoginRequiredMixin,ListView):
    model = Product
    template_name = "product.html"
    paginate_by = 10
    ordering = ["-created_at"]

