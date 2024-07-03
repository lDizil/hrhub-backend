from django.db import models
from user_app.models import User


class ServiceAccount(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    service_username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    app_password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
