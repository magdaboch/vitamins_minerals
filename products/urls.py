from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name = 'products_list'),
    path('wyszukaj/', views.search_products, name='search_products'),
]