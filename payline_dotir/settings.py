from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


SEND_URL = 'http://payline.ir/payment/gateway-send'
SEND_URL_TEST = 'http://payline.ir/payment-test/gateway-send'
PAYLINE_DOTIR_API_TEST = 'adxcv-zzadq-polkjsad-opp13opoz-1sdf455aadzmck1244567'
GATEWAY_URL = 'http://payline.ir/payment/gateway-'
GATEWAY_URL_TEST = 'http://payline.ir/payment-test/gateway-'
CHECK_URL = 'http://payline.ir/payment/gateway-result-second'
CHECK_URL_TEST = 'http://payline.ir/payment-test/gateway-result-second'

IS_PAYLINE_DOTIR_TEST = getattr(settings, 'IS_PAYLINE_DOTIR_TEST',
                                False)
try:
    PAYLINE_DOTIR_API = getattr(settings, 'PAYLINE_DOTIR_API')
except AttributeError:
    if IS_PAYLINE_DOTIR_TEST:
        pass
    raise ImproperlyConfigured("You need to define PAYLINE_DOTIR_API "
                               "in your settings module "
                               "to use the payline.ir payment processor.")
if not IS_PAYLINE_DOTIR_TEST:
    SEND_URL_FINAL = SEND_URL
    GATEWAY_URL_FINAL = GATEWAY_URL
    CHECK_URL_FINAL = CHECK_URL
    PAYLINE_DOTIR_API_FINAL = PAYLINE_DOTIR_API
else:
    SEND_URL_FINAL = SEND_URL_TEST
    GATEWAY_URL_FINAL = GATEWAY_URL_TEST
    CHECK_URL_FINAL = CHECK_URL_TEST
    PAYLINE_DOTIR_API_FINAL = PAYLINE_DOTIR_API_TEST
