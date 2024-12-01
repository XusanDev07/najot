from django.db import models


class Contact(models.Model):
    google_link = models.CharField(max_length=3000)
    phone = models.CharField(max_length=21)
    email = models.EmailField()
    address_uz = models.CharField(max_length=589)
    address_ru = models.CharField(max_length=589)
    address_en = models.CharField(max_length=589)
    telegram = models.CharField(max_length=589)
    insagram = models.CharField(max_length=589)
    facebook = models.CharField(max_length=589)
    twetter = models.CharField(max_length=589)
    tiktok = models.CharField(max_length=589)
    youtube = models.CharField(max_length=589)

    def contact_format(self):
        return {
            "id": self.id,
            "google_link": self.google_link,
            "phone": self.phone,
            "email": self.email,
            "address_uz": self.address_uz,
            "address_ru": self.address_ru,
            "address_en": self.address_en,
            "telegram": self.telegram,
            "insagram": self.insagram,
            "facebook": self.facebook,
            "twetter": self.twetter,
            "tiktok": self.tiktok,
            "youtube": self.youtube,
        }

    def __str__(self):
        return f"{self.google_link} | | {self.telegram}"
