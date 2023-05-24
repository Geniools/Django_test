from django.shortcuts import render
from django.http import HttpResponse


def index(request, n: str):
    # return HttpResponse(f"Hello there: {n}")
    context = {
        "passed_variable": n,
    }
    return render(request, 'main/index.html', context)
