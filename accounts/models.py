from __future__ import unicode_literals

from django.db import models

# Create your models here.
class balance(models.Model):
    username = models.ForeignKey(User)
    balance = models.IntegerField(default = 0)