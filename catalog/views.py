from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request="GET"):
    return render(request, 'catalog/home.html')

def contacts_page(request="GET"):
    return render(request, 'catalog/contacts.html')