from rest_framework import serializers
from .models import chat

class ChatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = chat
        fields = "__all__" #um alle felder zu bekommen
        # fields = ["id", "username", "massage", "date"]


