from django.urls import path

from . import views

app_name = 'noticias'

urlpatterns = [

    path('', views.listagem_categoria, name='home'),

    path('categorias/', views.listagem_categoria, name='listaCategorias'),

    path('categorias/<int:id>', views.detalhes_categoria, name='detalhesCategorias'),

    path('tags/', views.listagem_tags, name='listaTags'),

    path('tags/<int:id>/', views.detalhes_tag, name='detalhesTags'),

    path('noticias/', views.listagem_noticias, name='listaNoticias'),
    
    path('noticias/<int:id>/', views.detalhes_noticia, name='detalhesNoticias'),



]
