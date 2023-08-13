from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
#from django.http import HttpResponse
from catalog.models import Product, Version


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

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url=reverse_lazy('catalog:list')

    def get_initial(self):
        return {'owner': self.request.user}
    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url=reverse_lazy('catalog:list')

    def get_context_data(self, **kwargs):
        context_date=super().get_context_data(**kwargs)

        VersionFormSet=inlineformset_factory(Product, Version, VersionForm, extra=1)

        if self.request.method == "POST":
            context_date['formset']=VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_date['formset']=VersionFormSet(instance=self.object)

        return  context_date

    def form_valid(self, form):
        formset=self.get_context_data()['formset']
        self.object=form.save()

        if formset.is_valid():
            formset.instance=self.object
            formset.save()

        return super().form_valid(form)
