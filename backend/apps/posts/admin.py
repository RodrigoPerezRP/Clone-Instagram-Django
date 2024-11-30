from django.contrib import admin
from .models import (
    Post,
)

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'user')  
    search_fields = ('titulo', 'descripcion')  
    list_filter = ('fecha_creacion', 'user') 
    prepopulated_fields = {'slug': ('titulo',)}  
    ordering = ('-fecha_creacion',)  

admin.site.register(Post, PostAdmin)