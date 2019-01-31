from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', 'created_date', 'updated_date')

admin.site.register(BlogPost, BlogPostAdmin)
