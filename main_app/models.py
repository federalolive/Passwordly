from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Vault(models.Model):
    name = models.CharField(max_length=75)
    site = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    pw = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pw_id': self.id})

        