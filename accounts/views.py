from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, RegisterForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, smart_bytes


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
                user = register_form.save()
                login(request, user)
                return redirect("/")
    context = {
        "login_form": login_form,
        "register_form": register_form
    }
    return render(request, "accounts/login_and_register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

