from rest_framework import serializers
from my_testApp import models

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields='__all__'

class BlogSerializer(serializers.ModelSerializer):
    time_span=serializers.SerializerMethodField()
    author_name=serializers.ReadOnlyField(source='author.name') #for foriegn key
    #for more details on this
    author_details=AuthorSerializer(source='author',read_only=True)  #if foreign key name different we have to mention source
    # author=AuthorSerializer(read_only=True)  #during fetch it will come here and this will  become read only
    #during post or create drf automaticallly kicks out

    def get_time_span(self,obj):
        return f'{obj.created_at}-{obj.updated_at}'


    class Meta:
        model =models.Blog
        fields = ['id','blog_name', 'data', 'created_at', 'updated_at','tags',"author","time_span","author_name","author_details"]
        #to add all fileds
        # fields='__all__'
        # extra_kwargs={
        #     "data":{"read_only":True},
        #     "author":{"write_only":False}
        # }
        # read_only_fields=["data"]
        # write_only_fields=["author"] #in write only



    # def create(self, validated_data):
    #     blog=models.Blog(
    #         data="My Rules",
    #         author_id=3
    #     )
    #     return  blog