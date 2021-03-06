from django.urls import path, re_path
from users_auth.views import UserInfoView, SignInView, SignOutView, SignUpView


app_name = "users_auth"
urlpatterns = [
    # path('', UserInfoView.as_view(), name='user_info'),
    path('login/', SignInView.as_view(), name='user_sign_in'),
    path('logout/', SignOutView.as_view(), name='user_sign_out'),
    path('registration/', SignUpView.as_view(), name='user_sign_up'),
]