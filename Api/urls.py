from django.urls import path
from . import views

urlpatterns = [
    path('product-list', views.list_products),
    path('category-list', views.category_list),
    path('enter-list', views.enter_list),
    path('chiqim-list', views.expenditure),
    path('product-detail/<int:id>/', views.product_detail),
    path('categorys', views.category_list),
    path('category-detail/<int:id>/', views.category_detail)
]
