import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from user.serializers import PhysicianSerializer,PhysicianSerializerGet
from user.models import Individualphysician
from errormessage import Errormessage


class PreferredPhysician(generics.GenericAPIView):
    serializer_class = PhysicianSerializer

    def post(self, request):
        try:
            userid = request.data.get("UserId")
            familyid = request.data.get("FamilyMemberId")
            preferred = request.data.get("PreferredPhysician")
            model = Individualphysician.objects.filter(UserId_id=userid)
            physicianData = int(preferred)
            data = []
            for i in model:
                data.append(int(i.id))
            print(data)
            if familyid is None:
                if Individualphysician.objects.filter(UserId_id=userid).first():
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "UserId already exist try with another user"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
                else:
                    if physicianData not in data:
                        serializer = self.get_serializer(data=request.data)
                        serializer.is_valid(raise_exception=True)
                        user = serializer.save()
                        response = GenericResponse("message", "result", "status", "has_error")
                        response.Message = "Successful"
                        response.Result = PhysicianSerializer(user).data
                        response.Status = 200
                        response.HasError = False
                        jsonStr = json.dumps(response.__dict__)
                        return Response(json.loads(jsonStr), status=200)
            # elif Individualphysician.objects.filter(UserId_id=userid, FamilyMemberId_id=familyid).first():
            #     response = GenericResponse("message", "result", "status", "has_error")
            #     response.Message = "both userid and family id already exist"
            #     response.Result = False
            #     response.Status = 400
            #     response.HasError = True
            #     jsonStr = json.dumps(response.__dict__)
            #     return Response(json.loads(jsonStr), status=400)
            elif int(familyid) not in data:
                if Individualphysician.objects.filter(UserId_id=userid, FamilyMemberId_id=familyid).first():
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "both userid and family id already exist"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
                else:
                    if physicianData not in data:
                        serializer = self.get_serializer(data=request.data)
                        serializer.is_valid(raise_exception=True)
                        user = serializer.save()
                        response = GenericResponse("Message", "Result", "Status", "HasError")
                        response.Message = "Successful"
                        response.Result = PhysicianSerializer(user).data
                        response.Status = 200
                        response.HasError = False
                        jsonStr = json.dumps(response.__dict__)
                        return Response(json.loads(jsonStr), status=200)
               #  print("hello")
               # # if physicianData  in data:
               #  #if Individualphysician.objects.filter(UserId_id=userid, FamilyMemberId_id=familyid).first():
               #      response = GenericResponse("message", "result", "status", "has_error")
               #      response.Message = "both userid and family id already exist"
               #      response.Result = False
               #      response.Status = 400
               #      response.HasError = True
               #      jsonStr = json.dumps(response.__dict__)
               #      return Response(json.loads(jsonStr), status=400)
               #  else:
               #      print("hi")

            # elif int(familyid) not in data:
            #     response = GenericResponse("message", "result", "status", "has_error")
            #     response.Message = "user and familymember are different"
            #     response.Result = False
            #     response.Status = 400
            #     response.HasError = True
            #     jsonStr = json.dumps(response.__dict__)
            #     return Response(json.loads(jsonStr), status=400)
 
            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                return Response({
                    'Message': 'Successful',
                    'Result': PhysicianSerializerGet(user).data,
                    'HasError': False,
                    'Status': 200
                })
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = "User_id is must be unique"
            response.Result = [str(e)]
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
        #     if familyid is None:
        #         if physicianData not in data:
        #             serializer = self.get_serializer(data=request.data)
        #             serializer.is_valid(raise_exception=True)
        #             user = serializer.save()
        #             return Response({
        #                 'Message': 'Successful',
        #                 'Result': PhysicianSerializer(user).data,
        #                 'HasError': False,
        #                 'Status': 200
        #             })
        #
        #         else:
        #             response = GenericResponse("Message", "Result", "Status", "HasError")
        #             response.Message = " physician is already exist"
        #             response.Result = ""
        #             response.Status = 400
        #             response.HasError = True
        #             jsonStr = json.dumps(response.__dict__)
        #             return Response(json.loads(jsonStr), status=400)
        #     elif int(familyid) in data:
        #         if physicianData not in data:
        #             serializer = self.get_serializer(data=request.data)
        #             serializer.is_valid(raise_exception=True)
        #             user = serializer.save()
        #             response = GenericResponse("Message", "Result", "Status", "HasError")
        #             response.Message = "Successful"
        #             response.Result = PhysicianSerializer(user).data
        #             response.Status = 200
        #             response.HasError = False
        #             jsonStr = json.dumps(response.__dict__)
        #             return Response(json.loads(jsonStr), status=200)
        #
        #         else:
        #             if Individualphysician.objects.filter(UserId_id=userid, FamilyId_id=familyid).first():
        #                 response = GenericResponse("message", "result", "status", "has_error")
        #                 response.Message = "both userid and family id already exist"
        #                 response.Result = False
        #                 response.Status = 400
        #                 response.HasError = True
        #                 jsonStr = json.dumps(response.__dict__)
        #                 return Response(json.loads(jsonStr), status=400)
        #
        #     else:
        #         response = GenericResponse("Message", "Result", "Status", "HasError")
        #         response.Message = "please enter valid data"
        #         response.Result = False
        #         response.Status = 400
        #         response.HasError = True
        #         jsonStr = json.dumps(response.__dict__)
        #         return Response(json.loads(jsonStr), status=400)
        #
        # except Exception as e:
        #     response = GenericResponse("message", "result", "status", "has_error")
        #     response.Message = Errormessage(e)
        #     response.Result = False
        #     response.Status = 400
        #     response.HasError = True
        #     jsonStr = json.dumps(response.__dict__)
        #     return Response(json.loads(jsonStr), status=400)