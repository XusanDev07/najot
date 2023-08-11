from django.db import models
from najot.models import User


class Professions(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Clink(models.Model):
    name = models.CharField(max_length=128)
    info = models.TextField()
    img = models.ImageField("Clinka rasmi", upload_to="clink", null=True, blank=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Doktor(models.Model):
    name = models.CharField("Ism", max_length=128)
    familya = models.CharField("Familya", max_length=128)
    phone = models.CharField("Telefon raqam", max_length=20)
    img = models.ImageField("Rasm", upload_to="docs", null=True, blank=True)
    xona_raqami = models.SmallIntegerField(default=1)
    prof = models.ForeignKey(Professions, verbose_name="Shifokor Mutahasisligi", on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, verbose_name="Shifokor lavozimi", on_delete=models.SET_NULL, null=True)
    info_uz = models.TextField("Shifokor haqida qisqacha malumot")
    tajriba = models.SmallIntegerField()
    info_ru = models.TextField("Краткая информация о докторе")
    info_en = models.TextField("Brief information about the doctor")
    email = models.EmailField("Elektron pochta")
    gender = models.BooleanField("Jinsi", default=True)

    class Meta:
        verbose_name = "Doktor"
        verbose_name_plural = "1. Doktorlar"

    def doc_format(self):
        return {
            "doc_id": self.id,
            "doc_img": self.img.url if self.img.url else "",
            "doktor_name": self.name,
            "doktor_kasb": self.prof.name,
            "doc_info_uz": self.info_uz,
            "doc_info_ru": self.info_ru,
            "doc_info_en": self.info_en,
            "doc_phone": self.phone
        }

    def __str__(self):
        return f"{self.familya} {self.name}"


class DocTime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doc = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    free = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.date}: {self.doc.name}'


class Service(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    info_uz = models.TextField()
    info_ru = models.TextField()
    info_en = models.TextField()
    svg = models.CharField(max_length=10000)
    img = models.FileField(upload_to="services")
    doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    desktraptoin_uz = models.TextField()
    desktraptoin_ru = models.TextField()
    desktraptoin_en = models.TextField()

    def contact_format(self):
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
    
    def __str__(self):
        return self.name_uz
        


class DocReating(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Reating")
    doc = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    star = models.SmallIntegerField(choices=[
        (1, "     ⭐️ "),
        (2, "    ⭐️⭐️ "),
        (3, "   ⭐️⭐️⭐️ "),
        (4, "  ⭐️⭐️⭐️⭐️ "),
        (5, " ⭐️⭐️⭐️⭐️⭐️ ")
    ])

    feed = models.TextField()


class Price(models.Model):
    doc = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    price = models.CharField("Narxi", max_length=128, default="50 000 UZS")
    pr = models.IntegerField(editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.pr = int(self.price.replace(" ", "").replace("UZS", ""))
        for i in ["uzs", "usd", "$", "rub"]:
            self.pr = str(self.pr).replace(i, "")
        self.pr = int(self.pr)
        return super(Price, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.price} | {self.doc.name}"
