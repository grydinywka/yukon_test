from django.shortcuts import render
from django.views.generic.list import ListView
from blog.models import BlogPost


class PostsListView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = "blog/posts_list.html"

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context