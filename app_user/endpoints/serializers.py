from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.http import HttpResponse


class RegistrationSerializers(serializers.ModelSerializer):

    password2 = serializers.CharField(style = {'input_type':'password'},write_only = True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        password= self.validated_data['password']
        password2= self.validated_data['password2']
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({"Error":"This USername is already taken"})
        if password!=password2:
            raise serializers.ValidationError({'message':'password and password2 should be same'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email is already taken'})
        
        account= User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account

        
