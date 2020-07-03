from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product,Contact
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
    if request.method == "POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, "shop/contact.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def productview(request,id):
    product = Product.objects.filter(id=id)
    print(product)
    return render(request, "shop/product_view.html",{'product':product[0]})

def search(request):
    return render(request,"shop/search.html")

def checkout(request):
    return render(request,"shop/checkout.html")
