from django.db import models
from najot.models import User


class Professions(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Yonalishi"
        verbose_name_plural = "3. Yonalishlar"
    
    def __str__(self):
        return self.name


class Clink(models.Model):
    name = models.CharField(max_length=128)
    info = models.TextField()
    img = models.ImageField("Clinka rasmi", upload_to="clink", null=True, blank=True)

    class Meta:
        verbose_name = "Clinika"
        verbose_name_plural = "2. Clinikalar"
    
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField("Ism", max_length=128)

    class Meta:
        verbose_name = "Lavozm"
        verbose_name_plural = "4. Lavozmlar"
    
    def __str__(self):
        return self.name


class Doktor(models.Model):
    name = models.CharField("Ism", max_length=128)
    familya = models.CharField("Familya", max_length=128)
    phone = models.CharField("Telefon raqam", max_length=20)
    img = models.ImageField("Rasm", upload_to="docs", null=True, blank=True)

    prof = models.ForeignKey(Professions, verbose_name="Shifokor Mutahasisligi", on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, verbose_name="Shifokor lavozimi", on_delete=models.SET_NULL, null=True)
    info = models.TextField("Shifokor haqida qisqacha malumot")
    email = models.EmailField("Elektron pochta")
    gender = models.BooleanField("Jinsi", default=True)

    class Meta:
        verbose_name = "Doktor"
        verbose_name_plural = "1. Doktorlar"

    def __str__(self):
        return f"{self.familya} {self.name}"


class DocTime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doc = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    free = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Doktor Time"
        verbose_name_plural = "5. Doktorlar Vaqti"
    
    def __str__(self):
        return f'{self.doc} || {self.free}'


class Service(models.Model):
    name = models.CharField(max_length=128)
    info = models.TextField()
    icon = models.ImageField(upload_to="service")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "6. Servislar"
    
    def __str__(self):
        return self.name


# class DocReating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Reating")
#     doc = models.ForeignKey(Doktor, on_delete=models.CASCADE)
#     star = models.SmallIntegerField(choices=[
#         (1, "     ⭐️ "),
#         (2, "    ⭐️⭐️ "),
#         (3, "   ⭐️⭐️⭐️ "),
#         (4, "  ⭐️⭐️⭐️⭐️ "),
#         (5, " ⭐️⭐️⭐️⭐️⭐️ ")
#     ])
#     feed = models.TextField()


# class Price(models.Model):
#     doc = models.ForeignKey(Doktor, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     icon = models.ImageField(upload_to="service")


class DocReating(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="DocReatinguser")
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
    
    class Meta:
        verbose_name = "Narx"
        verbose_name_plural = "7. Narlar"

    def save(self, *args, **kwargs):
        self.pr = int(self.price.replace(" ", "").replace("UZS", ""))
        for i in ["uzs", "usd", "$", "rub"]:
            pr = pr.lower().replace(i, "")
        self.pr = int(pr)
        return super(Price, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.doc} || {self.service} || {self.price}'
    
