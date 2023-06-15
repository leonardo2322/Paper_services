from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from .models import Category
# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = 'listCategory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'listado_de_tareas'
        return context
