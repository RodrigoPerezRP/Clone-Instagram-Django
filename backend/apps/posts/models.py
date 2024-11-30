from django.db import models
from apps.usuarios.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    slug = models.SlugField(default="", null=False)
    imagen = models.ImageField(upload_to ='images/post')
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.titulo

