from django.db import models


class Xizmatlar(models.Model):
    name = models.CharField(max_length=128)
    img = models.FileField()

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "8. Xizmatlar"
    
    def __str__(self):
        return self.name

