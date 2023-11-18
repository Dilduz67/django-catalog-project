from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_categories():
    categories=None
    if CACHE_ENABLED:
        categories = cache.get('categories')

    if categories is None:
        categories = Category.objects.all()
        if CACHE_ENABLED:
            cache.set('categories', categories, 3600)

    return categories