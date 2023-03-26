from django.db import models
from .user import User

class HealthDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=255, unique=True)
    device_type = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
