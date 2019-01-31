from django.urls import path, re_path
from users_auth.views import UserInfoView


app_name = "users_auth"
urlpatterns = [
    path('', UserInfoView.as_view(), name='user_info'),
]