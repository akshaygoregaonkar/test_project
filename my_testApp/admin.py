from django.contrib import admin

# Register your models here.
from my_testApp.models import Blog,Author,Tag,BlogImage
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','created_at','data']
    ordering = ['created_at']

admin.site.register(Blog,BlogAdmin)

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(BlogImage)
