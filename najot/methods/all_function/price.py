from najot.models import Price


def price_in_doctor(request, params):
    a = Price.objects.filter(doc.doc_id=params["doktor_id"])
    return {
        "doktor_name": a.doc.name,
        "doktor_familya": a.doc.familya,
        "doktor_phone": a.doc.phone,
        "doc_img": a.doc.img.url if a.doc.img.url else "",
        "xizmat_turi_uz": a.service.name_uz,
        "xizmat_turi_ru": a.service.name_ru,
        "xizmat_turi_en": a.service.name_en,
        "doktor_info_uz": a.doc.info_uz,
        "doktor_info_ru": a.doc.info_ru,
        "doktor_info_en": a.doc.info_en,
        "xona_raqami": a.doc.xona_raqami,
        "xizmat_narxi": a.price,
        "tajriba": a.doc.tajriba,
        "des_uz": a.doc.info_uz,
        "des_ru": a.doc.info_ru,
        "des_en": a.doc.info_en,
    }
