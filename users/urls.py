from django.urls import path
from .views import SignUpView, LoginView, AdminLoginView, LogoutView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin-login/", AdminLoginView.as_view(), name="admin-login"),
]
