import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


















""""
@csrf_exempt
def index(request):
    if request.method=='GET':
        num=request.GET.get('number')
        print(num)
        return  HttpResponse('This is GET Request')
    elif request.method=="POST":
        print(request.body) #when we post data from body
        #this print gives us ugly string we cannot acces it
        print(json.loads(request.body))#so we have do json loads
        return  HttpResponse('This is my POST Request')
    else:
        return HttpResponse('This is not a get or post Request')
@csrf_exempt
def index_2(request):
    if request.method=='GET':
        number=request.GET.get('number')
        return  JsonResponse({ 'data':number})
    elif request.method=='POST':
        print(request.POST)

        return HttpResponse('this is my posy req')
        
"""