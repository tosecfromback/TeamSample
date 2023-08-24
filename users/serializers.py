from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

# from .models import *


### 회원가입
class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'name', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'비밀번호가 동일하지 않습니다.'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            name = validated_data.get('name'),
            email = validated_data.get('email'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user
    


### 로그인
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiedls = [ 'name', 'password']

    def validate(self, data):
        name= data.get('name')
        password = data.get('pasword')

        if not name:
            raise serializers.ValidationError('아이디를 입력해주세요')
        
        if not password:
            raise serializers.ValidationError('비밀번호를 입력해주세요.')
        
        user = authenticate(name=name, password=password)

        if user is None:
            raise serializers.ValidationError('아이디 및 비밀번호가 일치하지 않습니다.')
        
        return { "name" : name, "password" : password, "user" : user }


### 로그아웃
class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



### User 프로필 조회
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'name', 'email', 'last_login']