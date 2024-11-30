from django.contrib import admin
from .models import (
    Post,
)

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'idUsuario')  
    search_fields = ('titulo', 'descripcion')  
    list_filter = ('fecha_creacion', 'idUsuario') 
    prepopulated_fields = {'slug': ('titulo',)}  
    ordering = ('-fecha_creacion',)  