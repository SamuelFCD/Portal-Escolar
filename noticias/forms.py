from django import forms
from .models import Categoria, Tag


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }