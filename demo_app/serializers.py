from rest_framework import serializers
from demo_app import  models
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Blog
        fields=["id","created_at","title"]
        # fields='__all__' # to specify all fields
        # read_only_fields=["data"]
        extra_kwargs={"data":{"read_only":True}}
