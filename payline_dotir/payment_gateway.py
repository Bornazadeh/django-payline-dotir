# -*- coding: utf-8 -*-

import requests

# from django.utils.translation import ugettext as _

from .settings import SEND_URL_FINAL, GATEWAY_URL_FINAL
from .settings import CHECK_URL_FINAL  # , PAYLINE_DOTIR_API_FINAL


def send_url(amount, redirect_url, url, api):
    '''
    return payment gateway url to redirect user
    to it for payment.
    '''
    values = {'api': api, 'amount': amount, 'redirect': redirect_url}
    send_request = requests.post(SEND_URL_FINAL, data=values)
    id_get = send_request.text
    print(id_get)
    if int(id_get) > 0:
        print(".معتبر است id_get")
        payment_gateway_url = '%s%s' % (GATEWAY_URL_FINAL, id_get)
        return payment_gateway_url
    elif id_get == "-1":
        print(
            "‫‪ api‬ارسالی با نوع ‪ api‬تعریف شده در ‪ payline‬سازگار نیست.‬")
    elif id_get == "-2":
        print(
            "‫مقدار ‪ amount‬داده عددي نمی باشد و یا کمتر از 1000 ریال است.‬")
    elif id_get == "-3":
        print("‫مقدار ‪ redirect‬رشته ‪ null‬است.‬")
    elif id_get == "-4":
        print(
            "‫درگاهی با اطلاعات ارسالی یافت نشده و یا در حالت انتظار می باشد‬")
    else:
        print("some other error(s) occurred.")


def get_result(api, trans_id, id_get):
    '''
    Check if the given id_get and trans_id is from a valid transaction.
    '''
    check_values = {'api': api, 'id_get': id_get, 'trans_id': trans_id}

    check_transaction = requests.post(CHECK_URL_FINAL, data=check_values)
    result = check_transaction.text
    if result == "1":
        print(".‫تراکنش موفقیت آمیز بوده است‬")
        return True
    elif result == "-1":
        print(
            "‫‪ api‬ارسالی با نوع ‪ api‬تعریف شده در ‪ payline‬سازگار نیست.‬")
    elif result == "-2":
        print(".ارسال شده معتبر نمی باشد‬ trans_id")
    elif result == "-3":
        print(".‫id_get ارسال شده معتبر نمی باشد‬")
    elif result == "-4":
        print(".‫چنین تراکنشی در سیستم وجود ندارد و یا موفقیت آمیز نبوده است‬")
    else:
        print("some error(s) occurred, please try again.")
