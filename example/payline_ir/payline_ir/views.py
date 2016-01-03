from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
 
import requests

SEND_URL = 'http://payline.ir/payment/gateway-send'
SEND_URL_TEST = 'http://payline.ir/payment-test/gateway-send'
#PAYLINE_DOT_IR_API = settings.PAYLINE_DOT_IR_API
PAYLINE_DOT_IR_API_TEST = 'adxcv-zzadq-polkjsad-opp13opoz-1sdf455aadzmck1244567'
GATEWAY_URL = 'http://payline.ir/payment/gateway-'
GATEWAY_URL_TEST = 'http://payline.ir/payment-test/gateway-'
CHECK_URL = 'http://payline.ir/payment-test/gateway-result-second'
CHECK_URL_TEST = 'http://payline.ir/payment-test/gateway-result-second'


def pay_form(request):
    return render(request, 'pay_form.html')

def gateway(request):
    amount_post = request.POST['amount']
    amount = int(amount_post)
    #print("amount is %s" ) %type(amount)
    redirect_url = 'http://127.0.0.1:8000/result/'
    id_get = send(request,SEND_URL_TEST, PAYLINE_DOT_IR_API_TEST, amount, redirect_url)
    gateway_url='http://payline.ir/payment-test/gateway-' + id_get

    return redirect(gateway_url)

@csrf_exempt
def result(request):

    trans_id = request.POST['trans_id']
    id_get = request.POST['id_get']
    #trans_id = 362817
    #id_get = 13061
    #print("trans_id is %s") % trans_id
    #print("id_get is %s") % id_get
#    try:
#        amount = 11000 #int(amount_post)
#    except ValueError:
#        amount = 11000
#        print "NOT an integer"
#    trans['amount'] = amount
    #data = order_form.cleaned_data
#    print "amount is%s" %type(amount)
#    redirect_url = 'http://localhost/result'
    final_result = get(request, PAYLINE_DOT_IR_API_TEST, trans_id, id_get)
    
#    gateway_url='http://payline.ir/payment-test/gateway-' + id_get
#    print "gateway url is %s" % gateway_url
    #values = {'api': PAYLINE_DOT_IR_API_TEST}
    #gateway = requests.post(gateway_url, data=values, allow_redirects=True)
    if int(final_result) == 1:
        result_end = 'successful'
    else:
        result_end = 'UNsuccessful'

    return render(request, 'successful_payment.html', {'result_end': result_end})
#    return render(request, 'pay_form.html')
#    if 'q' in request.GET:
#        message = 'You searched for: %r' % request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#    return HttpResponse(message)

def send(request, url, api, amount, redirect):
    values = {'api': api, 'amount': amount, 'redirect': redirect}
    send_request = requests.post( url, data = values)
    id_get = send_request.text
    if int(id_get) > 0:
        gateway_url='http://payline.ir/payment-test/gateway-' + id_get
        return id_get

def get(request, api, trans_id, id_get):
    check_values = {'api': api, 'id_get': id_get, 'trans_id': trans_id}
    
    check_transaction = requests.post(CHECK_URL_TEST, data= check_values)
    result = check_transaction.text
    #if result == 1 :
    return result
