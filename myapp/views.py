
from django.shortcuts import render
from myapp.models import Product,Review
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home_view(request):
    return render(request, "home.html")


@login_required
def product_view(request):
    search_query = request.GET.get("search", "")
    product_list = Product.objects.all()

    if search_query:
        product_list = product_list.filter(name__icontains=search_query) 


    paginator = Paginator(product_list, 10) 
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    return render(request, "product.html", {
        "products": page_obj,
        "search": search_query,
    })


@login_required
def details_view(request, pk):
    product = Product.objects.get(pk=pk)
    review = Review.objects.filter(product=product)
    return render(request, "details.html", {
        "product": product,
        "review":review
    })

