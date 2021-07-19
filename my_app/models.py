from django.db import models

 # Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    created_at=models.DateTimeField()
    data=models.TextField()
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Blog'


# class article(models.Model):
#     author=models.CharField(max_length=50)
#     data=models.TextField()
#     created_at=models.DateTimeField()
#
#
#     class Meta:
#         db_table = 'article'

