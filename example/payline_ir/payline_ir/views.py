from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt

from payline_dotir.payment_gateway import send_url, get_result
from payline_dotir.settings import SEND_URL_FINAL, PAYLINE_DOTIR_API_FINAL


def pay_form(request):
    return render(request, 'pay_form.html')


def gateway(request):
    amount_post = request.POST['amount']
    amount = int(amount_post)

    redirect_url = 'http://127.0.0.1:8000/result/'
    gateway_url = send_url(amount, redirect_url,
                           SEND_URL_FINAL, PAYLINE_DOTIR_API_FINAL)

    return redirect(gateway_url)


@csrf_exempt
def result(request):

    trans_id = request.POST['trans_id']
    id_get = request.POST['id_get']

    final_result = get_result(PAYLINE_DOTIR_API_FINAL, trans_id, id_get)

    if int(final_result) == 1:
        result_end = 'successful'
    else:
        result_end = 'UNsuccessful'

    return render(request, 'successful_payment.html',
                  {'result_end': result_end})
