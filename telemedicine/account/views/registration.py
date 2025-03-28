from django.shortcuts import render, redirect
from django.contrib.auth import login


from ..forms import CustomUserRegistrationForm


def register_view(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = CustomUserRegistrationForm()

    return render(request, "account/registration.html", {"form": form})
