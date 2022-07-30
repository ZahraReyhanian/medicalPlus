from django.db.models import Q
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
import requests
import json
from .serializers import ResultSerializer, TestQuestionSerializer, TestSerializer
from .pagination import DefaultPagination
from .models import Test, TestResult

# Create your views here.
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE', 'PUT']:
            return [IsAdminUser()]
        
        # print(self.request.path) # /psychology/tests/4/
        #todo check prmission to store test
        return [AllowAny()]

    #todo save user status
    #todo update viewCount

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Test.objects.filter(pk=kwargs['pk']).update(viewCount=instance.viewCount + 1)
        serializer = TestSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)
    

    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def questions(self, request, pk):
        test = Test.objects.filter(pk=pk).get()
        serializer = TestQuestionSerializer(test)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def questionsresult(self, request, pk):
        #todo update user result
        result = request.data["result"]
        testresult = TestResult.objects.filter(test_id=pk).filter(Q(grade__gte=result)).order_by('grade').first()
        serializer = ResultSerializer(testresult)
        return Response(serializer.data)


# MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
# ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
# ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
# amount = 11000  # Rial / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# email = 'email@example.com'  # Optional
# mobile = '09123456789'  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://localhost:8000/psychology/verify/'


def send_request(request):
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
    req = requests.post(url="https://api.idpay.ir/v1.1/payment", data=json.dumps(
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
        req = requests.post(url="https://api.idpay.ir/v1.1/payment/verify", data=json.dumps(req_data), headers=req_header)

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