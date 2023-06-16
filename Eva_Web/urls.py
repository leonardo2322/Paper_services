from django.urls import path
from .views import *

urlpatterns = [
    path('', vistaHome ,name='home'),
    path("list/categories", CategoryListView.as_view(), name='category_list'),
    path("create/category", CreatItemCategory.as_view(), name="create_category")
]
