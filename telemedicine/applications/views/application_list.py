from django.shortcuts import render


def applications_list(request):

    return render(
        request,
        "applications/applications_list.html",
    )
