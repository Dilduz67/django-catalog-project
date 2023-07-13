from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.home_page),
    path('contacts/', views.contacts_page),
]