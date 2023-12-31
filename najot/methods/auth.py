import datetime, re, random, string, uuid
from methodism import custom_response, error_params_unfilled, MESSAGE, error_msg_unfilled, generate_key, code_decoder, \
    exception_data
from rest_framework.authtoken.models import Token
# from base.server import check_phone_in_db, check_token_in_db, update_token
# from base.sen_phone import send_phone
from najot.models.auth import User, OTP


def regis(requests, params):
    all_info = next((field for field in [
        'username', 'last_name', 'age', 'phone', 'token', 'password'
    ] if field not in params), '')

    if all_info:
        return custom_response(status=False, message=f"{all_info.capitalize()} parametrlari to'ldirilmagan")

    otp = OTP.objects.filter(key=params['token']).first()

    if not otp:
        return custom_response(False, {"Error": "Xato token !"})

    if otp.is_conf:
        return custom_response(False, {"Error": "Token eskirgan!"})

    user = User.objects.filter(phone=otp.phone).first()

    if user:
        return custom_response(False, {"Error": "Bu user band qilingan"})
    if len(params['password']) < 8 or params['password'].isalnum() or " " in params['password']:
        return custom_response(False, {
            "Error": "Parol 8ta belgi harf raqamdan iborat bo'lishi kerak"})

    user_data = {
        "password": params['password'],
        "username": params['username'],
        "phone": params.get('phone', ''),
    }

    if params.get('key', None):
        user_data.update({
            "is_staff": True,
            "is_superuser": True
        })

    userr = User.objects.create_user(**user_data)
    token = Token.objects.create(user=userr)
    return custom_response(False, {
        "Success": "Account yaratildi",
        "Token": token.key
    })


def login(request, params):
    not_data = 'phone' if 'phone' not in params else 'password' if 'password' not in params else ''
    if not_data:
        return custom_response(False, message=error_params_unfilled(not_data))

    user = User.objects.filter(phone=params['phone']).first()
    if not user:
        return custom_response(False, message=MESSAGE['UserNotFound'])

    if not user.check_password(params['password']):
        return custom_response(True, message=MESSAGE['UserPasswordError'])

    token = Token.objects.get_or_create(user=user)
    return custom_response(True, data={"succes": token[0].key})


def logout(request, params):
    token = Token.objects.filter(user=request.user).first()
    if token:
        token.delete()
    return custom_response(True, message=MESSAGE['LogedOut'])


def user_update(request, params):
    nott = 'password' if 'password' not in params else 'new_password' if 'new_password' not in params else ''
    if nott:
        custom_response(True, error_msg_unfilled(nott))
    if not request.user.check_password(params['password']):
        return custom_response(True, message={"Error": "Parol noto'g'ri"})

    if request.user.check_password(params['new_password']):
        return custom_response(True, message={"Error": "Parol eskisi bilan teng bo'lishi kerek emas"})

    if len(str(params['new_password'])) < 6 or params['new_password'].isalnum() or ' ' in params['new_password']:
        return custom_response(True, message=MESSAGE['ParamsNotFull'])
    request.user.set_password(params['new_password'])
    request.user.save()

    user = User.objects.filter(phone=params['phone']).first()

    if type(params['phone']) is not int and len(str(params['phone'])) < 12:
        error_msg = f"'{params['phone']}' phone 👈 12ta raqam"
        return custom_response(True, message=error_params_unfilled(error_msg))
    if user and user.id != request.user.id:
        return custom_response(True, message={"Error": "Bunaqa user band qilingan"})

    request.user.phone = params.get('phone', request.user.phone)
    request.user.username = params.get('username', request.user.phone)
    # request.user.phone = params.get('phone', request.user.phone)
    request.user.last_name = params.get('last_name', request.user.last_name)
    request.user.save()
    return custom_response(True, message={"Succes": "User update qilindi"})


def user_delete(request, params):
    request.user.delete()
    return custom_response(True, message=MESSAGE['UserSuccessDeleted'])


def check_phone(phone):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, phone):
        return True
    else:
        return False
