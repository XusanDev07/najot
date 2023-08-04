from django.db import models


class Xizmatlar(models.Model):
    name = models.CharField(max_length=128)
    img = models.FileField(),
