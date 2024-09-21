from django.db import models


# O perfil de cada gato deve incluir seu nome, descrição e imagem.

class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='Cats/', blank=True, null= True)

