from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employment(models.Model):
    title       = models.CharField(max_length= 100)
    job_type    = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    datetime    = models.CharField(max_length=20)

class Member(models.Model):
    """docstring for ."""
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    
