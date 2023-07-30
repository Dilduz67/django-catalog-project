from django.core.management import BaseCommand
from catalog.models import Product, Category

Product.objects.all().delete()
Category.objects.all().delete()

class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list  =[{'id': '1','name': 'Категория1', 'description': 'Описание1'},
                    {'id': '2','name': 'Категория2', 'description': 'Описание2'},
                    {'id': '3','name': 'Категория3', 'description': 'Описание3'}
                    ]
        
        category_fill =[]
        for category_item in category_list:
            category_fill.append(Category(**category_item))

        Category.objects.bulk_create(category_fill)
        
        product_list = [
                {'id': '1','name': 'Товар1', 'description': 'Описание1', 'preview': 'pic1.jpg', 'category': Category(id='1'),'price':'100','created':'20230101','last_upd':''},
                {'id': '2','name': 'Товар2', 'description': 'Описание2', 'preview': 'pic2.jpg', 'category':Category(id='2'),'price':'200','created':'20230202','last_upd':''},
                {'id': '3','name': 'Товар3', 'description': 'Описание3', 'preview': 'pic3.jpg', 'category':Category(id='3'),'price':'300','created':'20230303','last_upd':''},
                 ]

        product_fill =[]
        for product_item in product_list:
            product_fill.append(Product(**product_item))

        Product.objects.bulk_create(product_fill)