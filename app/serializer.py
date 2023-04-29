from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'nickname', 'comment')

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)