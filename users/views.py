from django.shortcuts import render
from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response, responses
from .models import *
from .forms import *
from .serializers import *

# Create your views here.

## View Version
class Index(View):
    def get(self, request):
        context = {
            'title' : 'UserIndex'
        }
        return render(request, 'users/index.html', context)
    def post(self, request):
        pass


    
class Signin(View):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class Signout(View):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class Login(View):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class Logout(View):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class UserDetail(View):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class UserUpdate(View):
    def get(self, request):
        pass
    def post(self, request):
        pass 


class UserPassChange(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

## APIView Version
class IndexAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass


    
class SigninAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class SignoutAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class LoginAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class LogoutAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class UserDetailAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class UserUpdateAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass 


class UserPassChangeAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass