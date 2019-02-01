from django.urls import path, re_path
from django.views.generic import TemplateView
from blog.views import PostsListView, PostDetailView, PostCreateView,\
                       PostUpdateView, PostDeleteView


app_name = "blog"
urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
