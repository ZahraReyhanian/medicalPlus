from django.shortcuts import redirect
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import requests
import json

from core.models import UserAccessContent
from .models import Order

X_API_KEY = "d9d94a3c-377a-4761-9757-a2c48e566b19"
IDP_API_PAYMENT = "https://api.idpay.ir/v1.1/payment"
IDP_API_VERIFY = "https://api.idpay.ir/v1.1/payment/verify"

CallbackURL = 'http://localhost:8000/order/verify/'

@api_view(['POST'])
def send_request(request):
    data = json.loads(request.body)['data']

    order = Order.objects.create(
        user_id=request.user.id,
        content_type_id=data['contentType'],
        object_id=data['id'],
        amount=data['price']
    )

    req_data = {
        "amount": data['price'],
        "order_id": order.id,
        "mail": data['email'],
        "callback": CallbackURL,
    }
    req_header = {"accept": "application/json",
                "content-type": "application/json",
                "X-API-KEY": X_API_KEY,
                "X-SANDBOX": "1"}

    req = requests.post(url=IDP_API_PAYMENT, data=json.dumps(
        req_data), headers=req_header)

    Order.objects.filter(pk=order.id).update(
        link=req.json()["link"],
        refID=req.json()["id"]
    )

    return HttpResponse(req)
    
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

    Order.objects.filter(pk=order_id).update(
        status=t_status
    )

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

        Order.objects.filter(pk=order_id).update(
            status=req.json()["status"],
            track_id=req.json()["payment"]["track_id"]
        )

        # create access if status = 100
        if req.json()["status"] == 100:
            order = Order.objects.filter(pk=order_id).first()
            access = UserAccessContent(
                order_id=order.id,
                user_id=order.user_id,
                content_type_id=order.content_type_id,
                object_id=order.object_id,
            )
            access.save()
            print(access.content_object.redirectLink)
            print('******************')
        
        

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
