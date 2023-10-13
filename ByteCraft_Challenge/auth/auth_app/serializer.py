from rest_framework import serializers
from .models import customuser, task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customuser
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            print(instance.password)
            instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}
