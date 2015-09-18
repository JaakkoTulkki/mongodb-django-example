from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.Serializer):
    pk = serializers.CharField(required=False)
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=500)

    def create(self, validated_data):
        User.objects.create(**validated_data)
        u = User.objects.get(username=validated_data.get("username"))
        return u
