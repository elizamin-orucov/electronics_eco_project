from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from .forms import LoginForm, RegisterForm, ResetPasswordForm, ResetPasswordComplete
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, smart_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages

User = get_user_model()


def login_and_register_view(request):
    login_form = LoginForm()
    register_form = RegisterForm()

    if request.method == "POST":
        submit = request.POST.get("submit")
        if submit == "login_form":
            login_form = LoginForm(request.POST or None)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect("/")
        else:
            register_form = RegisterForm(request.POST or None)
            if register_form.is_valid():
                new_user = register_form.save()
                uuid = urlsafe_base64_encode(smart_bytes(new_user.slug))
                token = PasswordResetTokenGenerator().make_token(new_user)
                link = request.build_absolute_uri(reverse_lazy("accounts:activation", kwargs={"uuid": uuid, "token": token}))
                send_mail(
                    "Electronics\n",
                    f"Linke kecid edib hesabinizi aktivlesdirin\n{link}",
                    settings.EMAIL_HOST_USER,
                    [new_user.email],
                    fail_silently=True
                )
                return redirect("/")
    context = {
        "login_form": login_form,
        "register_form": register_form
    }
    return render(request, "accounts/login_and_register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def activation_view_complete(request, uuid, token):
    slug = smart_str(urlsafe_base64_decode(uuid))
    user = User.objects.get(slug=slug)

    if not PasswordResetTokenGenerator().check_token(user, token):
        message = "Link duzgun deil!"
        messages.error(request, message)
        return redirect("accounts:login")
    user.is_active=True
    user.save()
    return redirect("/")


def reset_password_view(request):
    form = ResetPasswordForm()

    if request.method == "POST":
        form = ResetPasswordForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = get_object_or_404(User, email=email)
            uuid = urlsafe_base64_encode(smart_bytes(user.slug))
            token = PasswordResetTokenGenerator().make_token(user)
            link = request.build_absolute_uri(reverse_lazy("accounts:reset_password_complete", kwargs={"uuid": uuid, "token": token}))
            send_mail(
                "Reset Password",
                f"Please click link the bellow\n{link}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True
            )
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/reset_password.html", context)


def reset_password_complete(request, uuid, token):
    slug = smart_str(urlsafe_base64_decode(uuid))
    user = get_object_or_404(User, slug=slug)
    form = ResetPasswordComplete(instance=user)

    if not PasswordResetTokenGenerator().check_token(user, token):
        message = "Link duzgun deil!"
        messages.error(request, message)
        return redirect("accounts:login")

    if request.method == "POST":
        form = ResetPasswordComplete(instance=user, data=request.POST or None)

        if form.is_valid():
            form.save()
            return redirect("accounts:login-register")

    context = {"form": form}
    return render(request, "accounts/reset_password_complete.html", context)




