from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.views import APIView
from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from my_testApp import models
from django.db import transaction

# Create your views here.
from my_testApp.serializers import BlogSerializer



def get_all_blog(request):

    all_blog=models.Blog.objects.all()
    # all_blog=models.Blog.objects.filter(author__name='ram')
    response_blog = [ blog.to_json() for blog in all_blog]
    #method2
    """
    response_blog=[]
    for blog in all_blog:
        response_blog.append({
            'data':blog.data,
            'created_at':blog.created_at,
            'author':{
                "id":blog.author.id,
                'author_name':blog.author.name
            },
            "tags":[tag.tag_name for tag in blog.tags.all()]
        })
        """
    # print(type(blog.author))
    return JsonResponse(data={
        "all_blog":response_blog
    })
@csrf_exempt
def create_new_blog(request):
    req_data=json.loads(request.body)
    print(request.body)
    # models.Blog.objects.create(**req_data)
    models.Blog.objects.create(data=req_data['data'],author_id=req_data["author_id"])
    last_blog=models.Blog.objects.last()
    return JsonResponse(data={"blog":last_blog.to_json()})

@csrf_exempt
def update_blog(request,blog_id):
    if request.method !='PUT':
        return  JsonResponse(data={},status=403)
    req_data=json.loads(request.body)
    if not req_data.get('data') or not req_data.get('author_id'):
        return JsonResponse(data={'massage':'bad request'},status=400)
    blog=models.Blog.objects.get(id=blog_id)
    blog.data=req_data['data']

    blog.author_id=req_data['author_id']
    blog.save()
    return JsonResponse(data={"blog":blog.to_json()})
#normal delete
"""
@csrf_exempt
def delete_blog(request,blog_id):
    if request.method !="DELETE":
        return JsonResponse(data={},status=403)
    blog_image=models.BlogImage.objects.get(blog=blog_id)
    blog_image.delete()
    blog = models.Blog.objects.get(id=blog_id)
    blog.delete()
    return JsonResponse(data={"mgs":"Blog is deleted"},status=204)
"""

@csrf_exempt
def delete_blog(request,blog_id):
    if request.method !="DELETE":
        return JsonResponse(data={},status=403)
    try:
        with transaction.atomic():
            blog_image = models.BlogImage.objects.get(blog=blog_id)
            print(blog_image.image_url)
            blog_image.delete()
            print("here")
            blog_image = models.BlogImage.objects.get(blog=blog_id)
            print("here2")
            raise Exception()
            blog = models.Blog.objects.get(id=blog_id)
            blog.delete()
    except Exception:
        return  Response(data={"message":"something went weong"})

    return JsonResponse(data={"mgs":"Blog is deleted"},status=204)

#################DRF##########################
#djago views
@csrf_exempt
def get_or_create_blog(request):
    if request.method=="GET":
        all_blog = models.Blog.objects.all()
        # all_blog=models.Blog.objects.filter(author__name='ram')
        response_blog = [blog.to_json() for blog in all_blog]
        return JsonResponse(data={
            "all_blog": response_blog
        })
    elif request.method=="POST":
        req_data = json.loads(request.body)
        print(request.body)
        # models.Blog.objects.create(**req_data)
        models.Blog.objects.create(data=req_data['data'], author_id=req_data["author_id"])
        last_blog = models.Blog.objects.last()
        return JsonResponse(data={"blog": last_blog.to_json()})
    return HttpResponse(status=405)

@csrf_exempt
def update_or_delete_blog(request,blog_id):
    if request.method=="OPTIONS":
        return  JsonResponse(data={"allowed_methods":["put","delete","get","patch"]})
    if request.method=="PUT":
        req_data=json.loads(request.body)
        if  not req_data.get('data') or not req_data.get('author_id'):
            return JsonResponse(data={"messege":"bad request"},status=400)

        blog=models.Blog.objects.get(id=blog_id)
        print(blog.to_json())
        blog.data=req_data['data']
        blog.author_id=req_data['author_id']
        blog.save()
        print(blog.to_json())
        return JsonResponse(data={"updated blog":blog.to_json()})

    elif request.method=="DELETE":
        try:
            with transaction.atomic():
                blog_image = models.BlogImage.objects.filter(blog_id=blog_id)
                blog_image.delete()
                blog = models.Blog.objects.get(id=blog_id)
                blog.delete()
        except Exception:
            return HttpResponseBadRequest()
        return JsonResponse(data={"mgs": "Blog is deleted"}, status=204)
    elif request.method=="GET":
        blog = models.Blog.objects.get(id=blog_id)
        return  JsonResponse(data={"blog":blog.to_json()})
    elif request.method=="PATCH":
        return  JsonResponse(data={"method":f"patch req {blog_id}"})
    return HttpResponse(status=403)


############ DRF views #############
#drf views
"""
@api_view(['GET','POST'])
def get_or_create_drf_blog(request):
    if request.method=="GET":
        all_blog=models.Blog.objects.all()
        # all_blog = models.Blog.objects.filter(author_id=3)

        # response_blogs=[blog.to_json() for blog in all_blog]  #mannual serialize
        response_blogs=BlogSerializer(all_blog,many=True)
        # if we want last
        # response_blogs=BlogSerializer(all_blog.last())
        return Response(data=response_blogs.data)
    elif request.method=="POST":
        print(request.data)
        models.Blog.objects.create(data=request.data['data'], author_id=request.data["author_id"])
        last_blog=models.Blog.objects.last()
        return  Response(data={"method":"post req","data":last_blog.to_json()})

"""
@api_view(['GET','POST'])
def get_or_create_drf_blog(request):
    if request.method=="GET":
        all_blog=models.Blog.objects.all()
        response_blogs=BlogSerializer(all_blog,many=True)
        return Response(data=response_blogs.data)

    elif request.method=="POST":
        req_data=BlogSerializer(data=request.data) #json  => sql
        if req_data.is_valid():
            req_data.save()
        else:
            return  Response(status=status.HTTP_400_BAD_REQUEST,data=req_data.errors)
        last_blog=models.Blog.objects.last()
        response_blog=BlogSerializer(last_blog) #sql=>json
        return  Response(data={"method":"post req","data":response_blog.data})



@api_view(['PUT','DELETE','GET','PATCH'])
def update_or_delete_drf_blog(request,blog_id):
    if request.method == "PUT":
        req_data=request.data
        blog=models.Blog.objects.get(id=blog_id)
        blog_serializer=BlogSerializer(instance=blog,data=req_data)
        if blog_serializer.is_valid():
            blog_serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=blog_serializer.errors)
        update_blog=models.Blog.objects.get(id=blog_id)
        response_blog=BlogSerializer(update_blog)
        return Response(data={"blog":response_blog.data})
    elif request.method == "DELETE":
        try:
            with transaction.atomic():
                blog_image=models.BlogImage.objects.filter(blog_id=blog_id)
                blog_image.delete()
                blog=models.Blog.objects.get(id=blog_id)
                blog.delete()
        except Exception:
            return HttpResponseBadRequest()

        return Response(data={"mgs":"deleted"})
    elif request.method == "GET":
        blog=models.Blog.objects.get(id=blog_id)
        response_blog=BlogSerializer(blog)
        return Response(data=response_blog.data)
    elif request.method == "PATCH":
        return Response(data={"method": f"patch req {blog_id}"})


########### class based views#################

class Blog_Create_Retrive(APIView):
    def get(self,request):
        all_blog=models.Blog.objects.all()
        response_blog=BlogSerializer(all_blog,many=True)
        return Response(data=response_blog.data)
    def post(self,request):
        req_data=BlogSerializer(data=request.data)
        if req_data.is_valid():
            req_data.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=req_data.errors)
        last_created_blog=models.Blog.objects.last()
        response_blog=BlogSerializer(last_created_blog)
        return  Response(data={"blog":response_blog.data})

class Blog_Update_Delete(APIView):
    def put(self,request,blog_id):
        req_data=request.data
        blog=models.Blog.objects.get(id=blog_id)
        blog_serialier=BlogSerializer(instance=blog,data=req_data)
        if blog_serialier.is_valid():
            blog_serialier.save()
        else:
            return  Response(status=status.HTTP_400_BAD_REQUEST,data=req_data.errors)
        response_blog=BlogSerializer(blog_serialier)
        return Response(data={"blog":response_blog})
    def delete(self,blog_id):
        try:
            with transaction.atomic():
                blog_image = models.BlogImage.objects.get(blog_id=blog_id)
                blog_image.delete()
                blog = models.Blog.objects.get(id=blog_id)
                blog.delete()
        except:
            return Response(data={"mgs":"blog is deleted"})
    def get(self,request,blog_id):
        blog=models.Blog.objects.get(id=blog_id)
        response_blog = BlogSerializer(blog)
        return Response(data=response_blog.data)

######################### Generic Views ####################
class CreateRetrive_Blog(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = models.Blog.objects.all()
    # authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroy_Blog(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = models.Blog.objects.all()
    # authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]


########## token based Authentication ###############

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication ])
@permission_classes([IsAuthenticated])
def get_or_create_drflogin_blog(request):
    if request.method=="GET":
        all_blog=models.Blog.objects.all()
        response_blogs=BlogSerializer(all_blog,many=True)
        return Response(data={"blog":response_blogs.data,"user":request.user.username})

    elif request.method=="POST":
        req_data=BlogSerializer(data=request.data) #json  => sql
        if req_data.is_valid():
            req_data.save()
        else:
            return  Response(status=status.HTTP_400_BAD_REQUEST,data=req_data.errors)
        last_blog=models.Blog.objects.last()
        response_blog=BlogSerializer(last_blog) #sql=>json
        return  Response(data={"method":"post req","data":response_blog.data})




class Blog_Create_Retrive_token(APIView):
    authentication_classes=[TokenAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        all_blog=models.Blog.objects.all()
        print("im inside the view")
        response_blog=BlogSerializer(all_blog,many=True)
        return Response(data=response_blog.data)
    def post(self,request):
        req_data=BlogSerializer(data=request.data)
        if req_data.is_valid():
            req_data.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=req_data.errors)
        last_created_blog=models.Blog.objects.last()
        response_blog=BlogSerializer(last_created_blog)
        return  Response(data={"blog":response_blog.data})

@api_view(["POST"])
def login_user(request):
    username=request.data['username']
    password=request.data['password']
    #verify
    user=User.objects.get(username=username)
    if user.check_password(password):
        #now create token
        token, _=Token.objects.get_or_create(user_id=user.id)
        token.save()
        return Response(data={"mgs":"correct password","key":token.key})
    return Response(data={"mgs": "incorrect password"},status=401)

@api_view(["POST"])
def create_user(request):
    username=request.data['username']
    password=request.data['password']
    user=User.objects.create(username=username)
    user.set_password(password)
        #now create token
    token, _ =Token.objects.get_or_create(user_id=user.id)
    token.save()
    return Response(data={"mgs":"user created Successfully","key":token.key})

########## viewset ############

# class BlogViewSet(viewSet)
