from django.urls import  path
from demo_app import views
urlpatterns = [
path('blogs/',views.get_or_create_blogs,name="get_or_create_blogs" ),
path('blogs/<int:blog_id>/',views.update_or_delete_blogs,name="update_or_delete_blogs")
]