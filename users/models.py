from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user():
        pass

    def create_user():
        pass
        return self._create_user()
    
    def creates_superuser():
        pass
        return self._create_superuser()