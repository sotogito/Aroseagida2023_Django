from rest_framework import serializers
from .models import AddUserProfile

class AddUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUserProfile
        fields = '__all__'
