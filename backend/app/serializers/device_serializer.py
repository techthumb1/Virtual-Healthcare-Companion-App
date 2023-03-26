from rest_framework import serializers
from .models import HealthDevice

class HealthDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthDevice
        fields = ['id', 'device_id', 'device_type', 'device_name', 'date_added']
        read_only_fields = ['id', 'date_added']
