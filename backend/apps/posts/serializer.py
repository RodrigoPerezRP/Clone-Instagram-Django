from rest_framework import serializers
from django.utils import timezone
from .models import (
    Post
)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'titulo', 'descripcion', 'fecha_creacion', 'slug', 'imagen', 'user']

    def create(self, validated_data):
        if 'fecha_creacion' not in validated_data:
            validated_data['fecha_creacion'] = timezone.now()
        return super().create(validated_data)
        