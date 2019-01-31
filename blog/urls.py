from django.urls import path, re_path
from django.views.generic import TemplateView
from blog.views import PostsListView


app_name = "blog"
urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    # path('login/', SignInView.as_view(), name='user_sign_in'),
]