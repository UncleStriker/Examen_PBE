from rest_framework import serializers
from usuarios.models import User, Topico, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class TopicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topico
        fields = [
            'categoria'
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content'
        ]
