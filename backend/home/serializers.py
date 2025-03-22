from rest_framework import serializers





class SampleSerializer(serializers.Serializer):
    message = serializers.CharField(required=True, max_length=20)