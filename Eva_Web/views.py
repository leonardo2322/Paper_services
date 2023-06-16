
from django.shortcuts import render
from django.views.generic import ListView,CreateView
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Category
from .forms import FormCreateCategory
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