from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from hcpapi.serializer import HcpSerializer,HcpRegSerializer
from genericresponse import GenericResponse
import json
from hcpapi.models import HcpModel
from errormessage import Errormessage
from django.apps import apps

class GetAllDoctorsList(APIView):
    serializer_class = HcpRegSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = HcpModel.objects.all()
            serializer_class = HcpRegSerializer(queryset, many=True)
            model1 = apps.get_model('userappointment', 'AppointmentModel')

            c =model1.objects.all()
            b = len(c)

            for i in range(b):
                s= (model1.objects.values('Date')[i]['Date'])
                p= (model1.objects.values('Time')[i]['Time'])
                print(s)
                print(p)





            # a=model1.objects.all()
            # # print(a)
            # b = len(a)
            # # print(b)
            # dat=[]
            # tim=[]
            # for i in range(b):
            #     c = a[i]
            #     d =(c.Date,c.Time)
            #     dat.append(c.Date)
            #     tim.append(d)
            #
            # # print(dat)
            # toset=set(dat)
            # # print(toset)
            # n = list(toset)
            # s = (sorted(n))
            # print(s)




            # fromdate = model1.object.values_list('FromDate')
            # print(fromdate)
            # todate = model1.object.get('ToDate')
            # fromtime = model1.object.get('FromTime')
            # totime = model1.object.get('ToTime')
            # model2 = apps.get_model('userappointment', 'AppointmentModel')
            # date=model2.object.get('Date')
            # time=model2.object.get('Time')
            # if fromdate<=date<=todate:
            #     if fromtime<=time<=totime:

            return Response({'Message': 'Successful',
                             'Result': serializer_class.data,
                             'HasError': False,
                             'Status': 200})
        except HcpModel.DoesNotExist as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = []
            response.Status = 400
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
