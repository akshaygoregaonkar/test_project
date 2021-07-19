from django.db import models
from django.utils import  timezone

# Create your models here.
class Blog(models.Model):
    author=models.CharField(max_length=50)
    data=models.TextField()
    created_at=models.DateTimeField(default=timezone.now())
    title=models.CharField(max_length=50)


class Article(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(default=timezone.now())

    class Meta:
        db_table="Article"