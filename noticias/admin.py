from django.contrib import admin
from .models import Categoria, Tag, Perfil, Noticia


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    search_fields = ('titulo', 'texto')
    list_filter = ('categoria', 'tags')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Noticia, NoticiaAdmin)