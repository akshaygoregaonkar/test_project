from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    tag_name=models.CharField(max_length=50)
    def __str__(self):
        return self.tag_name


class Blog(models.Model):
    blog_name=models.CharField(max_length=50)
    data=models.TextField(default='')
    created_at=models.DateTimeField(default=timezone.now())
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Author,on_delete=models.PROTECT)
    tags=models.ManyToManyField(Tag)
    def to_json(self):
        return {
            "data":self.data,
            "blog_name":self.blog_name,
            "created_at":self.created_at,
            "updated_at":self.updated_at,
            "author":{
                "id":self.author.id,
                "author_name":self.author.name,
            },
            "tags":[tag.tag_name for tag in self.tags.all()]
        }
    def __str__(self):
        return self.blog_name
class BlogImage(models.Model):
    image_url=models.URLField()
    blog=models.OneToOneField(Blog,on_delete=models.PROTECT)
    def __str__(self):
        return self.image_url


