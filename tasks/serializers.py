from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        models = Task
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # Дополнительное поле для подтверждения пароля

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate(self, data):
        # Проверяем, совпадают ли пароли
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Пароли не совпали")
        return data

    def create(self, validated_data):
        # Убираем "password2" перед созданием пользователя
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    model=User
    field=("username","password")
    username = serializers.CharField()
    password = serializers.CharField()