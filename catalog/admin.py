from django.contrib import admin
from catalog.models import Product, Category

# Register your models here.

#admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'description',)
    list_filter = ('name',)
    search_fields = ('name', 'category',)