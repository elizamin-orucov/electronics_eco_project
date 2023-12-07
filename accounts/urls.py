from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/and/register/", views.login_and_register_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("activation/complete/<uuid>/<token>/", views.activation_view_complete, name="activation"),
]

