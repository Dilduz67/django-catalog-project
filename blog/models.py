from django.db import models
from django.utils.timezone import now

from catalog.models import NULLABLE

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=1000, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(verbose_name='изображение', **NULLABLE)
    create_date = models.DateTimeField(default=now, verbose_name='дата публикации', **NULLABLE)
    is_published = models.BooleanField(default=True,verbose_name='опубликовано')
    views_count = models.IntegerField(default=0,verbose_name='кол-во. просмотров',**NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


