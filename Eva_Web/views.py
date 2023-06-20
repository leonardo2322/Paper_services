
from typing import Any, Dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView,CreateView
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Category, Product
from .forms import FormCreateCategory, FormCreateProduct
from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# Create your views here.


def vistaHome(request):
    return render(request, 'home.html')
class CategoryListView(ListView):
    model = Category
    template_name = 'listCategory.html'
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        print(request)
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'listado_de_tareas'
        return context
class CreatItemCategory(CreateView):
    model = Category
    form_class = FormCreateCategory
    template_name = 'createItemCategory.html'
    success_url = reverse_lazy("category_list")
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Categoria'
        return context
    
class CreateItemProduct(CreateView):
    model = Product
    form_class = FormCreateProduct
    template_name = 'createProduct.html'
    def post(self, request, *args, **kwargs):
        data = {}
        try:
         action = request.POST['action']
         if action == 'add':
             form = self.get_form()
             if form.is_valid():
                 form.save()
                 data['success'] = 'se han ingresado los datos'
             else:
                 data = form.errors
         else:
             data['error'] = 'Ha ocurrido un error al insertar los datos'
        except Exception as e:
            print(e)
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Item Product'
        context['action'] = 'add'
        return context
    
class ListViewProduct(ListView):
    model = Product
    template_name = 'listProduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'listado de Productos'
        return context