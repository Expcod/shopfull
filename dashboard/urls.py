from . import views
from django.urls import path
from .views import export_enter_product_to_excel

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard),
    path('product-list', views.products),
    path('product-create', views.product_create),
    # enters
    path('enter-list', views.list_enter, name='list_enter'),
    path('enter-create', views.create_enter, name='create_enter'),
    path('enter-update/<int:id>/', views.update_enter, name='update_enter'),
    path('enter-delete/<int:id>/', views.delete_enter, name='delete_enter'),
    path('export-enter-products/', export_enter_product_to_excel, name='export_enter_products'),
    #chiqimlar
    path('order-list', views.expenditure, name='order_enter'),
]

