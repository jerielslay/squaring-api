from django.shortcuts import render
from django.http import HttpResponse
from django.views import View # Create your views here. 
# Create your views here.


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello world!')

class SquaringView(View):
    def get(self, request, number):
        return HttpResponse(number**2)
