from django.shortcuts import render


def results_list(request):

    return render(
        request,
        "results/results_list.html",
    )

