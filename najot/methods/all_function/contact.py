from najot.models import Contact


def all_contact(request, params):
    return {
        "result": [i.contact_format() for i in Contact.objects.all()]
    }

