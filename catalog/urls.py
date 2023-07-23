from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('contacts/', views.contacts_page),
] 