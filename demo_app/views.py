import json

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from demo_app.serializers import BlogSerializer

from demo_app import  models
# @csrf_exempt
# def get_blog(request):
#     if request.method=="GET":
#         all_blog=models.Blog.objects.all()
#         response_blog=[]
#         for blog in all_blog:
#             response_blog.append({"author":blog.author,"data":blog.data,"title":blog.title,"created_at":blog.created_at})
#
#         return JsonResponse(data={"blog":response_blog})
#     elif request.method=="POST":
#         rq_data=json.loads(request.body)
#         print(rq_data)
#         models.Blog.objects.create(**rq_data)
#         created_blog=models.Blog.objects.last()
#
#         return  JsonResponse(data={"created":created_blog.title})

@api_view(["GET","POST"])
def get_or_create_blogs(request):
    if request.method == "GET":
        all_blog = models.Blog.objects.all()
        response_blog=BlogSerializer(all_blog,many=True)
        return Response(data=response_blog.data)

    elif request.method == "POST":
        req_data =BlogSerializer(data=request.data)
        if req_data.is_valid():
            req_data.save()
        else:
            return  Response(status=status.HTTP_400_BAD_REQUEST,data=req_data.errors)
        created_blog = models.Blog.objects.last()
        response_blog=BlogSerializer(created_blog)
        return Response(data=response_blog.data)


@api_view(["GET","PUT","PATCH","DELETE"])
def update_or_delete_blogs(request):
    if request.method == "PUT":

        return Response(data={"blog": "Put"})
    elif request.method == "DELETE":

        return Response(data={"megs":"deletd"})
    elif request.method == "GET":

        return Response(data={"method": "get"})
    elif request.method == "PATCH":

        return Response(data={"Method": "patch"})


