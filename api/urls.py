from django.urls import path, re_path, include
from api.views import BlogPostView, BlogPostItemView


app_name = "api"
urlpatterns = [
    path('blogposts/', BlogPostView.as_view()),
    path('blogposts/<int:pk>/', BlogPostItemView.as_view()),
]
