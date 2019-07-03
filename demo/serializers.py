from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120,required=True)
    email = serializers.EmailField(required=True)
