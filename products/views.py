from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    # for p in products:
    #     raise Exception(p.product_vitamin.all()[0].valuevit_set.all()[0].value)
    return render(request, 'products_list.html', {"products": products})

def search_products(request):
    #     # if request.GET['reset_filters'] == '1':
    #     #     return redirect(to='products_list')
    filter_value = request.GET['filter_products'] if 'filter_products' in request.GET.keys() else ''
    products = Product.objects.filter(Q(product_vitamin__vitamin_symbol=filter_value) |
                                      Q(product_vitamin__vitamin_name=filter_value))\
                                        .order_by('-valuevit__value')
    products_mineral = Product.objects.filter(Q(product_mineral__mineral_name=filter_value)|
                                              Q(product_mineral__mineral_symbol=filter_value)) \
                                                .order_by('-valuemineral__value')
    # raise Exception(products)

    return render(request, 'search_product.html', {"products":products, "products_mineral":products_mineral,
                                                   "filter_value":filter_value})

@login_required
def add_product(request):
    pass