from djoser.serializers import UserCreateSerializer

from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User 
        fields = (
            'id',
            'email',
            'username',
            'last_name',
            'avatar',
            'date_joined',
        )