from django.db import models


class Dapp(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000, null=True, blank=True)  # submission owner
    status = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    homepage = models.CharField(max_length=1000)
    icon = models.CharField(max_length=1000, null=True, blank=True)
