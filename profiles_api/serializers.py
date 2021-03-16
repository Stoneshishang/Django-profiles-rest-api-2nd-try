from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView Serializer"""
    name = serializers.CharField(max_length=10)
