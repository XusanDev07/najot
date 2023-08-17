from django.db import models
from najot.models import User
from najot.models.services import Service
from datetime import datetime, timedelta


class Clink(models.Model):
    name = models.CharField(max_length=128)
    info = models.TextField()
    img = models.ImageField("Clinka rasmi", upload_to="clink", null=True, blank=True)

    def clink_format(self):
        return {
            "name": self.name,
            "info": self.info,
            "img": f"{self.img.url}"
        }

    def __str__(self):
        return self.name


class Doktor(models.Model):
    name = models.CharField("Ism", max_length=128)
    familya = models.CharField("Familya", max_length=128)
    phone = models.CharField("Telefon raqam", max_length=20)
    img = models.ImageField("Rasm", upload_to="docs", null=True, blank=True)
    xona_raqami = models.SmallIntegerField(default=1)
    services = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    info_uz = models.TextField("Shifokor haqida qisqacha malumot")
    tajriba = models.SmallIntegerField()
    info_ru = models.TextField("Краткая информация о докторе")
    info_en = models.TextField("Brief information about the doctor")
    gender = models.BooleanField("Jinsi", default=True)
    email = models.EmailField("Elektron pochta")
    dushanba = models.BooleanField("dushanba", default=True)
    seshanba = models.BooleanField("seshanba", default=True)
    chorshanba = models.BooleanField("chorshanba", default=True)
    payshanba = models.BooleanField("payshanba", default=True)
    juma = models.BooleanField("juma", default=True)
    is_active = models.BooleanField(default=True)

    def doc_format(self):
        return {
            "doc_id": self.id,
            "doc_img": self.img.url if self.img.url else "",
            "doktor_name": self.name,
            "doc_services": self.services.name_uz,
            "doc_info_uz": self.info_uz,
            "doc_info_ru": self.info_ru,
            "doc_info_en": self.info_en,
            "doc_phone": self.phone,
            "dushanba": self.dushanba,
            "seshanba": self.seshanba,
            "chorshanba": self.chorshanba,
            "payshanba": self.payshanba,
            "juma": self.juma,
        }

    def __str__(self):
        return f"{self.name}"


class DocTime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doc = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    free = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.date}: {self.doc.name}'


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
    price_doc = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    start = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
        current_time = datetime.now().time()
        end = (datetime.combine(datetime.now().date(), self.start) + timedelta(hours=1)).time()
        
        if self.start <= current_time <= end:
            self.status = False
        elif self.start <= current_time >= end:
            self.status = True
        

        doktor = Doktor.objects.get(id=self.price_doc_id)
        doktor.is_active = False
        doktor.save()

        super(Price, self).save(*args, **kwargs)

    def __str__(self):
        return self.price_doc.name



    # def save(self, *args, **kwargs):
    #     current_time = datetime.now().time()
        # bu kod ishlaydi faqat modellarga end degan timefield qo'shish kerak
    #     if self.start <= current_time <= self.end:
    #         self.status = False
    #     else:
    #         current_datetime = datetime.combine(datetime.now().date(), current_time)
    #         price_start_datetime = datetime.combine(datetime.now().date(), self.start)
    #         price_end_datetime = datetime.combine(datetime.now().date(), self.end)
            
    #         if (price_end_datetime - price_start_datetime) <= (current_datetime - price_start_datetime):
    #             self.status = True
    #         if current_time >= self.start and current_time <= self.end:
    #             self.status = False
         
        
    #     super(Price, self).save(*args, **kwargs)

    # def __str__(self):
    #     return f"{self.price} | {self.price_doc.name}"
