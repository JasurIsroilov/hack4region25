from django.contrib.auth import login
from django.shortcuts import render, redirect
from ..forms import LoginForm


def user_login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})

