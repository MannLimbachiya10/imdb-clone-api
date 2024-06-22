from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import Registration,LogoutNow

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',Registration,name='register'),
    path('logout/', LogoutNow, name='logout'),
]
