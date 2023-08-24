from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', views.Index.as_view(), name='main'),
]