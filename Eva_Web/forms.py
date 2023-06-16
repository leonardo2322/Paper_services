from django.forms import ModelForm,TextInput
from .models import Category



class FormCreateCategory(ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['autofocus'] = 'off'
    class Meta:
        model = Category
        fields = ['id', 'name']
        labels = {
            'name':'Nombre'
        }
        widgets= {
            'name': TextInput(attrs={
                "placeholder": "Ingrese el nombre de la categoria",
                'style':'width:17rem; margin: 10px 5px'
            })
        }