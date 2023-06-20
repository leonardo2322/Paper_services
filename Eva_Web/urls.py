from django.urls import path
from .views import *

urlpatterns = [
    path('', vistaHome ,name='home'),
    path("list/categories", CategoryListView.as_view(), name='category_list'),
    path("create/category", CreatItemCategory.as_view(), name="create_category"),
    path('create/product', CreateItemProduct.as_view(), name="create_product"),
    path('list/product', ListViewProduct.as_view(), name='list_Product')
]
