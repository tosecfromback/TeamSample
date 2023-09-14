from django.shortcuts import render
from django.views import View

# Create your views here.


class HttpsView(View):
    def get(self, request):
        context = {
            'title' : 'Test_Https'
        }
        return render(request, 'test/https_test.html', context)