from . import views
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard),
    path('product-list', views.products),
    path('product-create', views.product_create)
]