from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'specialty', 'date_time', 'location', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
