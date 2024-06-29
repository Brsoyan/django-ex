from django.db import models
import logging

logger = logging.getLogger(__name__)


# Create your models here.
class AddUser(models.Model):
    ip = models.CharField(max_length=45)
    location = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    check = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request from {self.ip} at {self.created_at}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Ping(models.Model):
    ip = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "Ping"
        verbose_name_plural = "Pings"
        ordering = ['-created_at']