from django.db import models

NULLABLE = {'null': True, 'blank': True}

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')
    created_at = models.DateTimeField(**NULLABLE)

    def __str__(self): 
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов
        ordering = ("name",)

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.CharField(max_length=500, verbose_name='описание')
    preview = models.ImageField (upload_to='images/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    created = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    last_upd = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения',**NULLABLE)

    def __str__(self): 
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар' # Настройка для наименования одного объекта
        verbose_name_plural = 'товары' # Настройка для наименования набора объектов
        ordering = ("name",)