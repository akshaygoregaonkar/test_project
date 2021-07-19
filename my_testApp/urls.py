from django.urls import path
from my_testApp import views
urlpatterns=[
path('blog/',views.get_all_blog, name='get_all_blog'),
path('create-blog/',views.create_new_blog, name='create_new_blog'),
path('update-blog/<int:blog_id>/',views.update_blog,name="update_blog"),
path('delete-blog/<int:blog_id>/',views.delete_blog,name="delete_blog"),
    ########################## DJango views ########################
path('django-blog/',views.get_or_create_blog,name="get_or_create_blog"),
path('django-blog/<int:blog_id>/',views.update_or_delete_blog,name="update_or_delete_blog"),

###### URL for  DRF DJango views######
path('drf-blog/',views.get_or_create_drf_blog,name="get_or_create_drf_blog"),
path('drf-blog/<int:blog_id>/',views.update_or_delete_drf_blog,name="update_or_delete_drd_blog"),

############################### classBased views ##########################
path('drf-class-blog/',views.Blog_Create_Retrive.as_view(),name="get_or_create_class_drf_blog"),
path('drf-class-blog/<int:blog_id>/',views.Blog_Update_Delete.as_view(),name="update_or_delete_class_drf_blog"),


############################## Generic Views ###########################################
path('drf-gclass-blog/',views.CreateRetrive_Blog.as_view(),name="get_or_create_gclass_drf_blog"),
path('drf-gclass-blog/<int:pk>/',views.RetrieveUpdateDestroy_Blog.as_view(),name="update_or_delete_gclass_drf_blog"),
#

############authecations urls ###############
path('drf-login-blog/',views.get_or_create_drflogin_blog,name="get_or_create_drflogin_blog"),
path('drf-loginclass-blog/',views.Blog_Create_Retrive_token.as_view(),name="Blog_Create_Retrive_token"),
    ######login ####
path('login/',views.login_user,name="login_user"),
path('create/',views.create_user,name="create_user")

]


#{"data":"my blog django","author_id":3}