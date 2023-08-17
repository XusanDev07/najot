from django.db import models


class Service(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    info_uz = models.TextField()
    info_ru = models.TextField()
    info_en = models.TextField()
    svg = models.CharField(max_length=10000)
    img = models.FileField(upload_to="services")
    price = models.CharField("Narxi", max_length=128, default="50 000 UZS")
    desktraptoin_uz = models.TextField()
    desktraptoin_ru = models.TextField()
    desktraptoin_en = models.TextField()

    def __str__(self):
        return self.name_uz

    def services_format(self):
        return {
            "id": self.id,
            "name_uz": self.name_uz,
            "name_ru": self.name_ru,
            "name_en": self.name_en,
            "info_uz": self.info_uz,
            "info_ru": self.info_ru,
            "info_en": self.info_en,
            "svg": self.svg,
        }
