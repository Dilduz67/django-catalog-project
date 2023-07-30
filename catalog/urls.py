from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name=CatalogConfig.name

urlpatterns = [
    path('', views.home_page, name="list"),
    path('contacts/<int:id>', views.contacts_page, name="details"),
] 