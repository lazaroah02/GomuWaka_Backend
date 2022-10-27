from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    topic = serializers.CharField(max_length = 200, required = False)
    message = serializers.CharField(max_length = 10000, required = False)