from django.shortcuts import render, redirect


def profile_view(request):
    if not request.user.is_authenticated:  # Check if user is logged in
        return redirect('/account/login/')
    if request.method == "GET":
        user = request.user
        user_data = {
            "first_name": user.first_name,
            "second_name": user.second_name,
            "patronymic": user.patronymic,
            "phone_number": user.phone_number,
            "email": user.email,
            "birth_date": user.birth_date
        }
        return render(
            request,
            "account/profile.html",
            context={
                "user_data": user_data
            })
