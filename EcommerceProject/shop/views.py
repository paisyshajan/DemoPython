from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category,Product

from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
# def index(request):
#     return HttpResponse('helooo')
def AllProdCat(request,cat_slug=None):
    cat_page=None
    prodcts_list=None
    if cat_slug!=None:
        cat_page=get_object_or_404(Category,slug=cat_slug)
        prodcts_list=Product.objects.all().filter(category=cat_page,available=True)
    else:
        prodcts_list=Product.objects.all().filter(available=True)

    paginator=Paginator(prodcts_list,6)     # paginator code starting
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'catpage':cat_page,'products':products})

def ProdctDetails(request,cat_slug,prod_slug):
    try:
        prdct=Product.objects.get(category__slug=cat_slug,slug=prod_slug)
    except Exception as e:
        raise e

    return render(request,'product.html',{'prodct':prdct})