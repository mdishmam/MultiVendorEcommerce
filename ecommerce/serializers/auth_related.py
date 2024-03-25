from rest_framework import serializers
# from django.contrib.auth.models import User
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'type')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if user.type == User.SELLER:
            user.is_staff = True
            user.save()
        return user
