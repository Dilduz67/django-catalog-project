from django.urls import path
from catalog.views import home_page, contacts_page, ProductCreateView, ProductUpdateView
from catalog.apps import CatalogConfig

app_name=CatalogConfig.name

urlpatterns = [
    path('', home_page, name="list"),
    path('contacts/<int:id>', contacts_page, name="details"),
    path('create/',ProductCreateView.as_view(), name="create_product"),
    path('update/<int:pk>',ProductUpdateView.as_view(), name="update_product")
]