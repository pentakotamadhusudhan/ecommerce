from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from user.serializers import FamilyMemberAddressSerializer
from errormessage import Errormessage


class FamilyMemberAddressView(generics.GenericAPIView):
    serializer_class = FamilyMemberAddressSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = FamilyMemberAddressSerializer(user).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "Please enter the valid data"
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message =  Errormessage(e)
            return Response({
                'Message': 'Successful',
                'Result': FamilyMemberAddressSerializer (user).data,
                'HasError': False,
                'Status': 200
            })

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
