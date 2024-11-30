from django.db import models
from apps.user.models import User
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now, null=True, blank=True)
    slug = models.SlugField(default="", null=False)
    imagen = models.ImageField(upload_to ='images/post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.titulo

