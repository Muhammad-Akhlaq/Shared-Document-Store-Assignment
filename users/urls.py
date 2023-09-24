from django.urls import path

from users.views import (
    UserAuthenticationView,
    UserDetailView,
    UserRegistrationView,
    UserTokenRefreshView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("login/", UserAuthenticationView.as_view(), name="user-login"),
    path("detail/", UserDetailView.as_view(), name="user-detail"),
    path("token/refresh/", UserTokenRefreshView.as_view(), name="user-token-refresh"),
]
