from django.urls import path

from . import views

app_name = 'noticias'

urlpatterns = [

    path('', views.listagem_categoria, name='home'),

    path('categorias/', views.listagem_categoria, name='listaCategorias'),

    path('categorias/<int:id>', views.detalhes_categoria, name='detalhesCategorias'),

    path('categorias/nova/', views.cadastrar_categoria, name='cadastrarCategoria'),
    
    path('categorias/<int:id>/editar/', views.atualizar_categoria, name='atualizarCategoria'),

    path('categorias/<int:id>/excluir/', views.excluir_categoria, name='excluirCategoria'),

    path('tags/', views.listagem_tags, name='listaTags'),

    path('tags/<int:id>/', views.detalhes_tag, name='detalhesTags'),

    path('tags/nova/', views.cadastrar_tag, name='cadastrarTag'),

    path('tags/<int:id>/editar/', views.atualizar_tag, name='atualizarTag'),

    path('tags/<int:id>/excluir/', views.excluir_tag, name='excluirTag'),

    path('noticias/', views.listagem_noticias, name='listaNoticias'),
    
    path('noticias/<int:id>/', views.detalhes_noticia, name='detalhesNoticias'),



]
