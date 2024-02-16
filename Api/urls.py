from django.urls import path
from . import views

urlpatterns = [
    path('product-list', views.list_products),
    path('category-list', views.category_list),
    path('enter-list', views.enter_list),
    path('chiqim-list', views.expenditure),
]
