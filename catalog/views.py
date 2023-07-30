from django.shortcuts import render
#from django.http import HttpResponse
from catalog.models import Product

# Create your views here.
def home_page(request):
    product_list = Product.objects.all()
    context = {"object_list" : product_list,
               "title": "Главная"
               }
    return render(request, 'catalog/home.html',context)

def contacts_page(request, id):
    product=Product.objects.get(pk=id)
    context = {"object": product,
               "title": "Детали"
               }
    return render(request, 'catalog/contacts.html',context)