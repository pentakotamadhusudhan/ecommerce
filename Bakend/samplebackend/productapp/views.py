from django.shortcuts import render
from .models import ProductsModel
from .serializers import ProductSerializer
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class ProductView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductsModel.objects.all()
    

   
    def post(self,request):
        try:
            ser = ProductSerializer(data=request.data)
            if ser.is_valid(raise_exception=True):
                if ser.save().id:
                    # print(ser.save().id)
                    return Response({
                        "status" : 200,
                        'result': ser.data,
                        'message':"success",

                    })
                else:
                    return Response({
                        "status" : 404,
                        'result': ser.data,
                        'message':"data Not saved "

                    })
        except Exception as e:
            return Response({
                "status" : 500,
                'result': e.args,
                'message':"success"

            })
   

class ProductViewGetByUser(ListAPIView):
    serializer_class = ProductSerializer 
   

    def get(self,request,id):
        # x =   get_object_or_404(ProductsModel,user_id =id)
        x = ProductsModel.objects.filter(user_id=id)
        print(x[0].image)
        print(request.build_absolute_uri(x[0].image))
        return Response({
                        "status" : 200,
                        'result': ProductSerializer(x,many= True).data,
                        'message':"products retrieve success "

                    })