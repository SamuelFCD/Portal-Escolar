from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import ProtectedError

from .models import Categoria, Tag, Noticia
from .forms import CategoriaForm, TagForm

def listagem_categoria(request): 

    context = {'categorias': Categoria.objects.all()}

    return render(request, 'noticias/listagem_categorias.html', context)

def detalhes_categoria(request, id):

    categoria = Categoria.objects.get(id=id)

    context = {'categoria': categoria}

    return render(request, 'noticias/detalhes_categoria.html', context)

def cadastrar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoria cadastrada com sucesso!')
        return redirect('noticias:listaCategorias')
    return render(request, 'noticias/form_categoria.html', {'form': form})


def atualizar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoria atualizada com sucesso!')
        return redirect('noticias:listaCategorias')
    return render(request, 'noticias/form_categoria.html', {'form': form})

def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, 'Categoria excluída com sucesso!')
        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.'
            )
        return redirect('noticias:listaCategorias')

    return render(request, 'noticias/confirmar_exclusao_categoria.html', {'categoria': categoria})


def listagem_tags(request): 

    context = {'tags': Tag.objects.all()}

    return render(request, 'noticias/listagem_tags.html', context)

def detalhes_tag(request, id):

    tag = Tag.objects.get(id=id)

    context = {'tag': tag}

    return render(request, 'noticias/detalhes_tags.html', context)

def cadastrar_tag(request):
    form = TagForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tag cadastrada com sucesso!')
        return redirect('noticias:listaTags')
    return render(request, 'noticias/form_tag.html', {'form': form})


def atualizar_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    form = TagForm(request.POST or None, instance=tag)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tag atualizada com sucesso!')
        return redirect('noticias:listaTags')
    return render(request, 'noticias/form_tag.html', {'form': form})

def excluir_tag(request, id):
    tag = get_object_or_404(Tag, id=id)

    if request.method == 'POST':
        tag.delete()
        messages.success(request, 'Tag excluída com sucesso!')
        return redirect('noticias:listaTags')

    return render(request, 'noticias/confirmar_exclusao_tag.html', {'tag': tag})

def listagem_noticias(request):

    context = {'noticias': Noticia.objects.all()}

    return render(request, 'noticias/listagem_noticias.html', context)

def detalhes_noticia(request, id):

    noticia = Noticia.objects.get(id=id)

    context = {'noticia': noticia}
    
    return render(request, 'noticias/detalhes_noticias.html', context)


