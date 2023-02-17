from django.http import JsonResponse
from .models import User_Details,Answer
from .serializers import RegistrationSerializer,AnswersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET','POST'])
def Registration_auth(request):
    if request.method=='GET':
        All_user=User_Details.objects.all()
        serial=RegistrationSerializer(All_user,many=True)
        return JsonResponse(serial.data, safe=False)
    if request.method=='POST':
        serial=RegistrationSerializer(data=request.data)
        #print(serial)
        if serial.is_valid():
            serial.save()
            return  Response( serial.data,status=status.HTTP_201_CREATED)
        else:
            return Response({'Message':serial.errors},status=status.HTTP_400_BAD_REQUEST)
    #pass
@api_view(['GET','POST'])
def Answers(request):
    if request.method=='GET':
        All_data=Answer.objects.all()
        serial=AnswersSerializer(All_data,many=True)
        return JsonResponse(serial.data, safe=False)
    if request.method=='POST':
        serial=AnswersSerializer(data=request.data)
        #print(serial)
        if serial.is_valid():
            serial.save()
            return  Response( serial.data,status=status.HTTP_201_CREATED)
        else:
            return Response({'Message':serial.errors},status=status.HTTP_400_BAD_REQUEST)




