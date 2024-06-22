from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your tests here.

class RegisterTestCase(TestCase):
    def test_register(self):
        self.client = APIClient()
        data={
            'username':'Mann123',
            'email':'mann.limbachiya@gmail.com',
            'password':'XYZ',
            'password2':'XYZ'
        }
        respone= self.client.post(reverse('register'), data)
        self.assertEqual(respone.status_code, status.HTTP_201_CREATED)
class LoginLogoutTestCase(TestCase):
    def setUp(self) -> None:
        self.user=User.objects.create_user(username='example',password='example@123') 
    def test_login(self):
        self.client=APIClient()
        data={
            'username':'example',
            'password':'example@123'
        }
        response=self.client.post(reverse('login'),data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_logout(self):
        self.client=APIClient()
        self.client.force_authenticate(user=self.user)
        self.token= Token.objects.get(user__username='example')
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)
        response=self.client.post(reverse('logout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        
