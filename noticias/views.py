from django.shortcuts import render

from .models import Categoria, Tag, Noticia 

def listagem_categoria(request): 

    context = {'categorias': Categoria.objects.all()}

    return render(request, 'noticias/listagem_categorias.html', context)

def detalhes_categoria(request, id):

    categoria = Categoria.objects.get(id=id)

    context = {'categoria': categoria}

    return render(request, 'noticias/detalhes_categoria.html', context)

def listagem_tags(request): 

    context = {'tags': Tag.objects.all()}

    return render(request, 'noticias/listagem_tags.html', context)

def detalhes_tag(request, id):

    tag = Tag.objects.get(id=id)

    context = {'tag': tag}

    return render(request, 'noticias/detalhes_tags.html', context)

def listagem_noticias(request):

    context = {'noticias': Noticia.objects.all()}

    return render(request, 'noticias/listagem_noticias.html', context)

def detalhes_noticia(request, id):

    noticia = Noticia.objects.get(id=id)

    context = {'noticia': noticia}
    
    return render(request, 'noticias/detalhes_noticias.html', context)


