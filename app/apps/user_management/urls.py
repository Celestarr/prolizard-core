from django.urls import path

from .views import LoginView, LogoutView, RegistrationView

app_name = "user_management"  # pylint: disable=invalid-name

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegistrationView.as_view(), name="registration"),
]
