from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.Serializer):
    pk = serializers.Field()
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return User.objects.create(**validated_data)