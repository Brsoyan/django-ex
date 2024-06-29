from rest_framework import serializers
from .models import AddUser, Ping

class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUser
        fields = ['ip', 'location', 'os', 'info']

class PingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ping
        fields = ['ip', 'created_at']
