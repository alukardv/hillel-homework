from rest_framework import serializers

from apps.authentication.models import User, UserManager, ActivationToken


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "email"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
