from najot.methods.auth import regis, login, logout, user_update, user_delete
from najot.methods.all_function.doktor import doc_list, doc_add, doc_delete, professions, position, clink, doc_id, \
    get_clink, doctime_id, all_doc
from najot.methods.all_function.contact import all_contact
from najot.methods.all_function.price import price_in_doctor
from najot.methods.all_function.services import services_id, all_services

ununsable_variable = dir()


def all_methods(request, params):
    return {
        "result": [x for x in ununsable_variable if "__" not in x]
    }
