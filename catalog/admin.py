from django.contrib import admin
from catalog.models import Product, Category, Version


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

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product','version_number','version_name')
    list_filter = ('product',)