from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SigninForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = '__all__'

        
class LoginForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = '__all__'