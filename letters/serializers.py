from rest_framework import serializers
from .models import PrevLetter

class PrevLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrevLetter
        fields = '__all__'