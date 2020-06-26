from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil
# Create your views here.
def index(request):
    products = Product.objects.all();
    allProds = []
    catProds =  Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    print(cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = ceil(n/4)
        allProds.append([prod,range(1,nslides),nslides])


    params = {'allProds':allProds} 
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("contact page")

def tracker(request):
    return HttpResponse("tracker page")

def productview(request):
    return HttpResponse("product view page")

def search(request):
    return HttpResponse("search page")

def checkout(request):
    return HttpResponse("checkout page")
