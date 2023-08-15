from django.contrib import admin
from najot.models.docktor_qushish import Doktor, Price, DocTime, Clink
from najot.models.services import Service
from najot.models.contact import Contact


admin.site.register(Doktor)
admin.site.register(Price)
admin.site.register(DocTime)
admin.site.register(Clink)
admin.site.register(Service)
admin.site.register(Contact)
