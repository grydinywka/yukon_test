from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from blog.models import BlogPost
from blog.forms import PostCreateForm


class PostsListView(LoginRequiredMixin, ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = "blog/posts_list.html"

    def get_queryset(self):
        return BlogPost.objects.all()


class PostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "post_object"


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'blog/post_create.html'
    success_url = '/blog/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, 'Post with id {} created'.format(self.object.id))
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Error during creating the post!')
        return super().form_invalid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostCreateForm
    template_name = 'blog/post_update.html'
    success_url = "/blog/"
    context_object_name = "post_object"
    model = BlogPost

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.created_by:
            messages.add_message(self.request, messages.INFO, 'Post #{} was created of other user!'.format(
                self.object.id))
            return redirect('blog:posts')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Post with id {} updated'.format(self.object.id))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Error during updating post {}!'.format(self.object.id))
        return super().form_invalid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = '/blog/'
    template_name = 'blog/post_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.created_by:
            messages.add_message(self.request, messages.INFO, 'Post #{} was created of other user!'.format(
                self.object.id))
            return redirect('blog:posts')
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Post with id {} deleted'.format(kwargs['pk']))
        return super().delete(request, *args, **kwargs)


