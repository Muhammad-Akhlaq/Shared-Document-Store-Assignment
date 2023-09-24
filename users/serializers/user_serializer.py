from django.db.models import Q
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        existing_user = User.objects.filter(
            Q(email=validated_data["email"]) | Q(username=validated_data["username"])
        ).first()
        if existing_user:
            if existing_user.username == validated_data["username"]:
                raise serializers.ValidationError(
                    "Username already exists.", code="unique"
                )
            if existing_user.email == validated_data["email"]:
                raise serializers.ValidationError(
                    "Email already exists.", code="unique"
                )
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
