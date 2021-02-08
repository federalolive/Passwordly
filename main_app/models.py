from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random

class Passwd(models.Model):
    name = models.CharField(max_length=100)
    