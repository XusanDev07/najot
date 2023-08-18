from django.db import connection
from django.http import JsonResponse
from methodism import custom_response

from najot.models import Service


def services_id(request, params):
    if params['pk']:
        services = Service.objects.filter(id=params['pk']).first()
        return {
            "id": services.id,
            "Xizmat turi": services.name_uz,
            "Icon": services.svg,
            'narxi': services.price
        }


def all_services(request, params):
    return {
        "result": [i.services_format() for i in Service.objects.all()]
    }
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM najot_service ;")
    #     columns = [col[0] for col in cursor.description]
    #     results = cursor.fetchall()
    # services = [dict(zip(columns, row)) for row in results]
    # return custom_response(status=True, message={"result": services})
