from datetime import datetime
from methodism import custom_response
from najot.models import Price, Doktor, User


def price_in_doctor(request, params):
    doc = params['doc_id']
    start = str(params['start'])
    # created_by = User.objects.filter(id=request.user.id).first()
    if doc is not None and start:
        start = datetime.strptime(start, '%H:%M:%S').time()
        created_by = User.objects.filter(id=params['user_id']).first()
        Price.objects.create(price_doc_id=doc, start=start, created_by=created_by)

    # if a is None:
    #     return {
    #         'error': "Bunday doktorga oid narx mavjud emas."
    #     }

    return {
        "Success"
    }

    # if "doktor_id" not in params:
    #     return {
    #         "error": "doktor_id paramsda bolishi kerak"
    #     }
    # try:
    #     d = Doktor.objects.filter(id=params["doktor_id"]).first()
    #     a = Price.objects.filter(doc=d).first()
    # except:
    #     return {
    #         "error": "Doktor yoki Price topilmadi"
    #     }
    #
    # if a is None or not a:
    #     return {
    #         "error": "Doktor yoki Price topilmadi"
    #     }
    #
    # return {
    #     "doktor_name": a.doc.name,
    #     "doktor_familya": a.doc.familya,
    #     "doktor_phone": a.doc.phone,
    #     "doc_img": a.doc.img.url if a.doc.img.url else "",
    #     "xizmat_turi_uz": a.service.name_uz,
    #     "xizmat_turi_ru": a.service.name_ru,
    #     "xizmat_turi_en": a.service.name_en,
    #     "doktor_info_uz": a.doc.info_uz,
    #     "doktor_info_ru": a.doc.info_ru,
    #     "doktor_info_en": a.doc.info_en,
    #     "xona_raqami": a.doc.xona_raqami,
    #     "xizmat_narxi": a.price,
    #     "tajriba": a.doc.tajriba,
    #     "des_uz": a.doc.info_uz,
    #     "des_ru": a.doc.info_ru,
    #     "des_en": a.doc.info_en,
    #     "gender_bobo": a.doc.gender
    # }
