from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        models = Task
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "pass1", "pass2")

    def validate(self, data):
        if data["pass1"] != data["pass2"]:
            raise serializers.ValidationError("Пароли не совпали")
        raise data

    def create(self, validated_data):
        validated_data.pop("pass2")
        user = User.objects.create_user(**validated_data)
        return user
