from methodism import custom_response, exception_data
from najot.models.docktor_qushish import Doktor, Clink, DocTime
from najot.serializer.all import DocSerializer


def clink(request, params):
    prof = Clink.objects.filter(name=params['name']).first()
    if prof:
        return custom_response(status=False, message={"Bunday lavozim bor"})
    Clink.objects.create(name=params['name'])
    return custom_response(status=True, message="Succes")


def get_clink(request, params):
    return {
        "clink": [[
            x.name,
            x.info,
            x.img.url
        ] for x in Clink.objects.all()]
    }


def professions(request, params):
    prof = Professions.objects.get(name=params['name'])
    Professions.objects.get_or_create(params['name'])
    return custom_response(status=True, message="Succes")


def position(request, params):
    prof = Position.objects.filter(name=params['name']).first()
    if prof:
        return custom_response(status=False, message={"Bunday lavozim bor"})
    Position.objects.create(name=params['name'])
    return custom_response(status=True, message="Succes")


def doc_list(request, params):
    a = Doktor.objects.all()
    serializer = DocSerializer(a, many=True)
    return custom_response(status=True, message=serializer.data)


def doc_add(request, params):
    request.FILES.get('image')
    try:
        serializer = DocSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return custom_response(status=True, message={"suucess"})
        # return custom_response(status=False, message={"Error"})
    except Exception as e:
        return custom_response(False, message='UndefinedError', data=exception_data(e))


def doc_delete(request, params):
    try:
        doc = Doktor.objects.get(id=params['pk'])
        doc.delete()
        return custom_response(status=True, message="True")
    except Doktor.DoesNotExist:
        return custom_response(status=False, message={"error": "Doktor topilmadi"})


def doc_id(request, params):
    if params['pk']:
        doc = Doktor.objects.filter(id=params['pk']).first()
        return {
            "id": doc.id,
            "doc_name": doc.name,
            "doc_familya": doc.familya,
            "doc_phone": doc.phone,
            "doc_img": doc.img.url if doc.img.url else "",
            "doc_prof": doc.prof.name,
            "doc_position": doc.position.name,
            "doc_info_uz": doc.info_uz,
            "doc_info_ru": doc.info_ru,
            "doc_info_en": doc.info_en,
            "doc_email": doc.email,
            "doc_gender": doc.gender
        }


def doctime_id(request, params):
    if params['pk']:
        doctime = DocTime.objects.filter(doc=params['pk']).first()
        return {
            "doktor_kuni": doctime.date,
            "doctor_vaqti": doctime.time,
            "dockor_ismi": doctime.doc.name
        }


def all_doc(request, params):
    return {
        "result": [i.doc_format() for i in Doktor.objects.all()]
    }


