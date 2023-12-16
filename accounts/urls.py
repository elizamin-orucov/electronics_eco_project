from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/and/register/", views.login_and_register_view, name="login-register"),
    path("logout/", views.logout_view, name="logout"),
    path("activation/complete/<uuid>/<token>/", views.activation_view_complete, name="activation"),
    path("reset/password/", views.reset_password_view, name="reset-password"),
    path("reset/password/complete/<uuid>/<token>/", views.reset_password_complete, name="reset_password_complete")
]

