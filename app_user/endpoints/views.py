from .serializers import RegistrationSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from app_user.models import create_auth_token #when you are using normal Token method
#from rest_framework_simplejwt.tokens import RefreshToken #whenyou need to use jwt tokens
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema()
@api_view(['POST'])
def LogoutNow(request):
    request.user.auth_token.delete()
    return Response({'message':'Token deleted successfully!!'})

@swagger_auto_schema(method='POST' ,request_body=RegistrationSerializers)
@api_view(['POST'])
def Registration(request):
    if request.method == 'POST':
        serializer = RegistrationSerializers(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            my_dict={}
            my_dict['Response']="Registration is successfull!!"
            my_dict['username']= account.username
            my_dict['email']=account.email
            my_dict['Token']=Token.objects.get(user=account).key
           # refresh = RefreshToken.for_user(account)
            # my_dict['Token']={
            #                     'refresh': str(refresh),
            #                     'access': str(refresh.access_token),
            #                     }
            return Response(my_dict,status.HTTP_201_CREATED)
        return Response(serializer.errors)