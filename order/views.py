from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

IDP_API_PAYMENT = "https://api.idpay.ir/v1.1/payment"
IDP_API_VERIFY = "https://api.idpay.ir/v1.1/payment/verify"

CallbackURL = 'http://localhost:8000/order/verify/'


def send_request(request):
    #request data :
    #content_type_id
    #object
    #user_id
    req_data = {
        "amount": "2000",
        "order_id": "11",
        "name": "zahra",
        "callback": CallbackURL,
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json",
                  "X-API-KEY": "d9d94a3c-377a-4761-9757-a2c48e566b19",
                  "X-SANDBOX": "1"}
    req = requests.post(url=IDP_API_PAYMENT, data=json.dumps(
        req_data), headers=req_header)

    print(req.json())
    return redirect(req.json()["link"])
    # print(req.json())
    # if isinstance(req.json()["data"], dict):
    #     authority = req.json()["data"]["authority"]
    # if len(req.json()['errors']) == 0:
    #     return redirect(ZP_API_STARTPAY.format(authority=authority))
    # else:
    #     e_code = req.json()['errors']['code']
    #     e_message = req.json()['errors']['message']
    #     return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")

@csrf_exempt
def verify(request):  
    t_status = request.POST.get('status')
    id = request.POST.get('id')
    order_id = request.POST.get('order_id')
    if t_status == "10":
        req_header = {"accept": "application/json",
                      "content-type": "application/json",
                      "X-API-KEY": "d9d94a3c-377a-4761-9757-a2c48e566b19",
                      "X-SANDBOX": "1"}
        req_data = {
            "id": id,
            "order_id": order_id,
        }
        req = requests.post(url=IDP_API_VERIFY, data=json.dumps(req_data), headers=req_header)

        return HttpResponse(req)
        # if len(req.json()['errors']) == 0:
        #     t_status = req.json()['data']['code']
        #     if t_status == 100:
        #         return HttpResponse('Transaction success.\nRefID: ' + str(
        #             req.json()['data']['ref_id']
        #         ))
        #     elif t_status == 101:
        #         return HttpResponse('Transaction submitted : ' + str(
        #             req.json()['data']['message']
        #         ))
        #     else:
        #         return HttpResponse('Transaction failed.\nStatus: ' + str(
        #             req.json()['data']['message']
        #         ))
        # else:
        #     e_code = req.json()['errors']['code']
        #     e_message = req.json()['errors']['message']
        #     return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user!!!!!!!!')
