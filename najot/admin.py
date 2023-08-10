from django.contrib import admin
from najot.models.docktor_qushish import Doktor, Price, Position, DocTime, Professions, Clink, Service
from najot.models.contact import Contact


admin.site.register(Doktor)
admin.site.register(Price)
admin.site.register(Position)
admin.site.register(Professions)
admin.site.register(DocTime)
admin.site.register(Clink)
admin.site.register(Service)
admin.site.register(Contact)
