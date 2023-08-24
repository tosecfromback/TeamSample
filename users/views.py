from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
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
        return render(request, 'users/APIList.html', context)
    def post(self, request):
        pass

class FuncCheck(View):
    def get(self, request):
        context = {
            'title' : 'FunctionCheck'
        }
        return render(request, 'users/logincheck.html',context)
    def post(self, request):
        pass


    
class Signin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('users:index')
        form = SigninForm()
        context = {
            'form' : form,
            'title' : '회원가입'
        }
        return render(request, 'users/signin.html', context)
    
    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('users:login')
        context = {
            'form' : form
        }
        return render(request, 'users/login.html', context)



class Signout(View):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('users:check')
        
        form = LoginForm()
        context = {
            'form' : form,
            'title' : '로그인'
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('users:check')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('users:check')
            
        form.add_error(None, '아이디가 없습니다')

        context = {
            'form' : form
        }

        return render(request, 'users/login.html', context)



class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('users:index')
    def post(self, request):
        pass 



class UserDetail(View):
    def get(self, request):
        context = {
            'title' : '프로필 조회'
        }
        return render(request, 'users/profile.html', context)
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
    def post(self, request):
        serializer = LoginSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            response = Response(
                {
                    "user" : { "id" : user.pk, "name" : user.name },
                    "message" : "로그인 완료"
                },
                status = status.HTTP_200_OK
            )
            return response
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutAPI(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass 



class UserDetailAPI(APIView):
    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    def post(self, request):
        user = request.user
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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