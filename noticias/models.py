from django.db import models

from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Noticia(models.Model):

    titulo = models.CharField(max_length=200)

    texto = models.TextField()

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='noticias')

    tags = models.ManyToManyField(Tag, related_name='noticias')

    def __str__(self): 
        return self.titulo
