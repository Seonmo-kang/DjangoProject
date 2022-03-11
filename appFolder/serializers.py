from rest_framework import serializers
from .models import Info,Hospital

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
    def create(self, validated_data):
        return Info.objects.create(**validated_data)

class HospitalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
