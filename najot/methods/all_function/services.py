from najot.models import Service


def services_id(request, params):
    if params['pk']:
        services = Service.objects.filter(id=params['pk']).first()
        return {
            "id": services.id,
            "Xizmat turi": services.name_uz,
            "Icon": services.svg,
            "Doktrning_ismi": services.doktor.name,

        }


def all_services(request, params):
    return {
        "result": [i.services_format() for i in Contact.objects.all()]
    }
    
