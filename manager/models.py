import uuid as uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    room = models.IntegerField(null=True)
    id_number = models.CharField(max_length=9)
    initial_contract_date = models.CharField(max_length=10)
    final_contract_date = models.CharField(max_length=10)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    date = models.DateField()
    hour = models.CharField(max_length=50)


class MaintenanceRequestRelevance(models.IntegerChoices):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    EMERGENCY = 4


class MaintenanceRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    relevance = models.IntegerField(choices=MaintenanceRequestRelevance.choices)
    creation_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


# Class TenantContract IS NOT WORKING, it doesn't cause problems but it doesn't work
class TenantContract(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    file = models.FileField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
