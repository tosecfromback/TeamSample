from django.urls import path
from .views import HttpsView

app_name = 'test'

urlpatterns = [
    path('', HttpsView.as_view(), name='test_main'),
]